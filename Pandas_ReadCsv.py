# -*- coding: utf-8 -*-
"""
CODIGO_EVALUACIÓN 
@author: Kevin
"""

import pandas as pd
#import numpy as np

DataSet_csv=pd.read_csv('PANDAS/archivos cargados/bestsellers-with-categories.csv'
                        ,sep=',',
                        names=['Nombre','Autor','Raiting de usuarios','Vistas','Precio','Año','Genero'])
#print(DataSet_csv.tail(10))
DF_BestSeller=pd.DataFrame(DataSet_csv)
#print(DF_BestSeller)
OptionsColumns={'A':['Nombre'],'B':['Autor'],'C':['Raitting de Usuarios'],'D':['Visitas'],'E':['Precio'],'F':['Año'],'G':['Genero']}
DT_Columns=pd.DataFrame(OptionsColumns)

def Fields(Arg1):
    CountCols=Arg1.count(',')
    #print(CountCols)
    FilterSplit=Arg1.upper().split(sep=(','))    
    #print('----',FilterSplit)
    ListColumns=''    
    for options in FilterSplit:
        #print(options)        
        if options == 'A':
            ListColumns="Nombre" + ", "
            #print(ListColumns)
        elif options=="B":
            ListColumns=ListColumns + "Autor" + ", "
            #print(ListColumns)
        elif options=="C":
            ListColumns=ListColumns + "Raitting de Usuarios"  + ", "
            #print(ListColumns)
        elif options=="D":
            ListColumns=ListColumns + "Visitas"  + ", "
            #print(ListColumns)
        elif options=="E":
            ListColumns=ListColumns + "Precio"  + ", "
            #print(ListColumns)
        elif options=="F":
            ListColumns=ListColumns + "Año"  + ", "
            #print(ListColumns)
        elif options=="G":
            ListColumns=ListColumns + "Genero" + ", "
            #print(ListColumns)
    ListColumns=ListColumns[0:(len(ListColumns)-2)]
    return ListColumns
#--------------------------------------------------------
def FilterData(SelectedFields,GetDS):
    Count=SelectedFields.count(', ')
    #print('tipo: ',type(SelectedFields))
    EnumFields=SelectedFields.split(sep=(', '))    
    #print('count: ', Count, 'Enum: ', EnumFields)
    try:
        if Count==0:
            Field0=SelectedFields
            ReturnsDS=GetDS[Field0]
        elif Count==1:
            Field0=EnumFields[0]
            Field1=EnumFields[1]
            ReturnsDS=GetDS[[Field0,Field1]]
        elif Count==2:
            Field0=EnumFields[0]
            Field1=EnumFields[1]
            Field2=EnumFields[2]
            #print('debug',Field0,Field1,Field2)
            ReturnsDS=GetDS.loc[:,[Field0,Field1,Field2]]
        elif Count==3:
            Field0=EnumFields[0]
            Field1=EnumFields[1]
            Field2=EnumFields[2]
            Field3=EnumFields[3]
            ReturnsDS=GetDS[[Field0,Field1,Field2,Field3]]
        elif Count==4:
            Field0=EnumFields[0]
            Field1=EnumFields[1]
            Field2=EnumFields[2]
            Field3=EnumFields[3]
            Field4=EnumFields[4]
            ReturnsDS=GetDS[[Field0,Field1,Field2,Field3,Field4]]
        elif Count==5:
            Field0=EnumFields[0]
            Field1=EnumFields[1]
            Field2=EnumFields[2]
            Field3=EnumFields[3]
            Field4=EnumFields[4]
            Field5=EnumFields[5]
            ReturnsDS=GetDS[[Field0,Field1,Field2,Field3,Field4,Field5]]
        elif Count==6:
            Field0=EnumFields[0]
            Field1=EnumFields[1]
            Field2=EnumFields[2]
            Field3=EnumFields[3]
            Field4=EnumFields[4]
            Field5=EnumFields[5]
            Field6=EnumFields[6]
            ReturnsDS=GetDS[[Field0,Field1,Field2,Field3,Field4,Field5,Field6]]
    except:
        print('error generando dataset: ', ValueError())
        ReturnsDS=GetDS   
    #print(ReturnsDS)        
    return ReturnsDS
#-------------------------------------------    
print(DT_Columns)
ColumnFilter=input('Ingresa los identificadores de los campos que deseas visualizar, separadas por comas (Ejem:A,B,G)= ')
try:   
    ColsView=Fields(ColumnFilter)
    print('campos condicionales: ',ColsView)
    DataSet_csv=FilterData(ColsView, DataSet_csv)
    print(DataSet_csv.head())   
except:
    print('Ocurrio un error durante el proceso: ')    




