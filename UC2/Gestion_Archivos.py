# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:15:44 2022

@author: Miguel
"""

import os
#Para crear archivo, recibe como parametro el nombre del archivo
# y e l contenido del archivo

def crear_archivos(nombre, contenido):
    archivo = open(nombre, "wt")
    archivo.write(contenido)
    archivo.close()

# para eliminar recibe como parametro el nombre del archivo a eiminar
def eliminar_archivo(nombre):
    os.remove(nombre)

#para gregar contenido a un archivo plano, debe existir un archivo
# se envia como parametro el nombre y el contenido del archivo

def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n " + contenido)
    archivo.close()

#para leer un archivo, ya debe existir un rachivo plano
#ejmplo: txt, py, java ..
#Recibe como parametro el nombre del archivo a leer
#y devuelve el contenido del archivo
 
def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido