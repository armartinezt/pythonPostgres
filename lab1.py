# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 14:28:45 2016

@author: amt
"""

import os, csv, re
import psycopg2, psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import numpy

conexion2=psycopg2.connect(host="localhost",port=5433,user="postgres",password="admin14",database="midb")
conexion2.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)   


def main():
    #print('hola')
    crearBasepg()
    #crearTabla()
    #consultaTabla()
    #insertarTabla()
    #leerCSV()
    
archivoCSV = "C:/ic/dlh/Dataset/voice.csv"

def limpiaCampo(campo):
    nombreCampo = re.findall(r'[A-Za-z0-9_]{2,30}',campo )
        
    return nombreCampo[0]


def leerCSV():
    try:
        with open(str(archivoCSV)) as ArchCSV:
            leer = csv.reader(ArchCSV,delimiter=",", dialect=csv.excel,quoting=csv.QUOTE_NONE)
            for row in leer:
                print(row)
                
    except Exception as e:
        print("leerCSV-Error: "+str(e))
    finally:
            ArchCSV.close()    
            
def crearBasepg():
    try:
        conexion=psycopg2.connect(host="localhost",port=5433,user="postgres",password="admin14")
        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conexion.cursor()
        cur.execute('CREATE DATABASE midb2')
        conexion.commit()
        print("Base de datos creada")
    except Exception as e:
        print("Error: "+str(e))
        
    finally:
        cur.close()
        
def crearTabla():
    try:
        cur = conexion2.cursor()
        cur.execute('CREATE TABLE mitabla(id SERIAL NOT NULL, articulo VARCHAR(20) NOT NULL)')
        conexion2.commit()
        print("Tabla creada")
    except Exception as e:
        print("Error: "+str(e))
        
def consultaTabla():
    try:
        cur = conexion2.cursor()
        cur.execute("SELECT * FROM voice")
        rows= cur.fetchall()
        print(rows)
    except Exception as e:
        print("Error: "+str(e))
        
def insertarTabla():
    try:
        cur = conexion2.cursor()
        cur.execute("INSERT INTO mitabla (articulo) VALUES('Lab1') ")
        conexion2.commit()
        print("Registro insertado...")
    except Exception as e:
        print("Error: " +str(e))
        
    
if __name__ == '__main__':
    main()
    

