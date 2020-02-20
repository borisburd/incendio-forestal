# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import random
import matplotlib.pyplot as plt
import numpy as np
def probabilidad_deseada(valor_max):
    p=random.random()
    if p<valor_max:
        p=True
    elif p>=valor_max:
        p=False
    return(p)
def crear_bosque(cant_arboles):
    bosque=[]
    for i in range(cant_arboles):
        bosque.append(0)
    return(bosque)
def primavera(l,p):
    for i in range(len(l)):
        valor=probabilidad_deseada(p)
        if valor:
            l[i]=1
        elif valor:
            l[i]==0
    return(l)
def rayos(l,f):
    for i in range(len(l)):
        valor=probabilidad_deseada(f)
        if valor:
            l[i]=-1
    return(l)
def propagacion(l):
    for i in range(len(l)-1):
        if l[i]==-1:
            if l[i+1]!=0:
                l[i+1]=-1
    for i in range(len(l)-1,0,-1):
        if l[i]==-1:
            if l[i-1]!=0:
                l[i-1]=-1
    return(l)      
def limpieza(l):
    for i in range(len(l)):
        if l[i]==-1:
            l[i]=0
    return(l)
def incendio_forestal(rep,arboles_iniciales,p,f):
    bosque=crear_bosque(arboles_iniciales)
    count=0
    valores=[]
    for i in range(rep):
        bosque=primavera(bosque,p)
        bosque=rayos(bosque,f)
        bosque=propagacion(bosque)
        bosque=limpieza(bosque)
        for i in range(len(bosque)):
            if bosque[i]==1:
                count+=1
        valores.append(count)
        count=0
    return(np.mean(valores))
def graficar_promedio(rep_promedio,rep,arboles_iniciales,p,f):
    lista_promedio=[]
    x_value=[]
    for i in range(rep_promedio):
        x_value.append(i)
    for i in range(rep_promedio):
        promedio=incendio_forestal(rep,arboles_iniciales,p,f)
        lista_promedio.append(promedio)
    grafico=plt.plot(x_value,lista_promedio)
    plt.show(grafico)
    
graficar_promedio(50,50,100,0.8,0.02)
