import pandas as pd 
import sys
import ftfy as f
from datetime import *
from  FUNCIONES import *

filepath_output =r'C:/Users/PC - Usuario/Desktop/TESIS/ARCHIVOS/ARCHIVOS_PROCESADOS'
filepath_input = 'C:/Users/PC - Usuario/Desktop/PRUEBAS_ETL/TABLAS/Clientes.csv' 

class Clientes(): 
          def __init__(self,COD_DISTRIBUIDORA,COD_CLIENTE,	COD_VENDEDOR,	NOMBRE_CLIENTE,	TIPO_DOC_CLIENTE	,NUM_DOC_CLIENTE	,TIPO_NEGOCIO_CLIENTE	,DISTRITO_CLIENTE,	RUTA_ENTREGA, ESTADO_CLIENTE): 
               self.COD_DISTRIBUIDORA = COD_DISTRIBUIDORA 
               self.COD_CLIENTE = COD_CLIENTE
               self.COD_VENDEDOR = COD_VENDEDOR
               self.NOMBRE_CLIENTE = NOMBRE_CLIENTE
               self.TIPO_DOC_CLIENTE = TIPO_DOC_CLIENTE
               self.NUM_DOC_CLIENTE = NUM_DOC_CLIENTE
               self.TIPO_NEGOCIO_CLIENTE = TIPO_NEGOCIO_CLIENTE
               self.DISTRITO_CLIENTE = DISTRITO_CLIENTE
               self.RUTA_ENTREGA = RUTA_ENTREGA 
               self.ESTADO_CLIENTE = ESTADO_CLIENTE
    
          def Grabar(self, dfc): 
               conexion=odbc.connect(db_connector())   
               cursor = conexion.cursor() 

               try:  
                         cursor.execute("BEGIN TRANSACTION")
                         for index, row in dfc.iterrows():  
                              self.COD_DISTRIBUIDORA = row['COD_DISTRIBUIDORA'] 
                              self.COD_CLIENTE = row['COD_CLIENTE']
                              self.COD_VENDEDOR = row['COD_VENDEDOR']
                              self.NOMBRE_CLIENTE = row['NOMBRE_CLIENTE']
                              self.TIPO_DOC_CLIENTE = row['TIPO_DOC_CLIENTE']
                              self.NUM_DOC_CLIENTE = row['NUM_DOC_CLIENTE']
                              self.TIPO_NEGOCIO_CLIENTE = row['TIPO_NEGOCIO_CLIENTE']
                              self.DISTRITO_CLIENTE = row['DISTRITO_CLIENTE']
                              self.RUTA_ENTREGA = row['RUTA_ENTREGA'] 
                              self.ESTADO_CLIENTE = row['ESTADO_CLIENTE']


                              Insert="""INSERT INTO CLIENTES (COD_DISTRIBUIDORA, COD_CLIENTE, COD_VENDEDOR, NOMBRE_CLIENTE, TIPO_DOC_CLIENTE, NUM_DOC_CLIENTE, TIPO_NEGOCIO_CLIENTE, DISTRITO_CLIENTE, RUTA_ENTREGA, ESTADO_CLIENTE) 
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
               
                              cursor.execute(Insert,(
                                     self.COD_DISTRIBUIDORA, 
                                     self.COD_CLIENTE, 
                                     self.COD_VENDEDOR, 
                                     self.NOMBRE_CLIENTE, 
                                     self.TIPO_DOC_CLIENTE, 
                                     self.NUM_DOC_CLIENTE, 
                                     self.TIPO_NEGOCIO_CLIENTE, 
                                     self.DISTRITO_CLIENTE, 
                                     self.RUTA_ENTREGA, 
                                     self.ESTADO_CLIENTE
                                     ))
                              conexion.commit() 
               
               except Exception as e: 
                         conexion.rollback()
                         print(f"Error al grabar Clientes: {e}")
               finally: 
                         print('CARGÓ CORRECTAMENTE CLIENTES A BD')
                         conexion.close()

if filepath_input.endswith('.csv'):
     separador = detectar_separador(filepath_input) 
     fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
     dfc= pd.read_csv(filepath_input, delimiter = separador, encoding='unicode_escape',dtype='string') 
     num_columnas = dfc.shape[1]  
     print ("Tiene la siguiente cant de columnas : ", num_columnas) 

     #dfc.info()
     ###TRANSFORMACION
     #VALIDACIÓN DE FORMATO DE COLUMNAS ADMITIDAS PARA EL PROCESO 


     print(dfc.head(100)) 
     print(dfc.info())
     if num_columnas == 10 :
          dfc= corregir_columnas_CLIENTES(dfc) 
          print(dfc.head(98))
          print("Todo ok") 
          TESTINSTANCE = Clientes(None, None, None, None, None, None, None, None, None, None)
          TESTINSTANCE.Grabar(dfc)
          nombre_tabla="CLIENTES"
          nombre_output = f"{filepath_output}\\{nombre_tabla}_{fecha_actual}.csv" 
          dfc.to_csv(nombre_output, index=False)
          print(f"Archivo procesado guardado como {nombre_output}")
          
     else : 
          print("Faltan columnas , se detiene el proceso.") 
          sys.exit() 

elif filepath_input.endswith('.txt'): 
     separador = detectar_separador(filepath_input) 
     fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
     dfc= pd.read_csv(filepath_input, delimiter = separador, encoding='unicode_escape',dtype='string') 
     num_columnas = dfc.shape[1]  
     print ("Tiene la siguiente cant de columnas : ", num_columnas) 

     #dfc.info()
     ###TRANSFORMACION
     #VALIDACIÓN DE FORMATO DE COLUMNAS ADMITIDAS PARA EL PROCESO 
     print(dfc.head(100)) 
     print(dfc.info())
     if num_columnas == 10 :
          dfc= corregir_columnas_CLIENTES(dfc) 
          print(dfc.head(98))
          print("Todo ok") 
          TESTINSTANCE = Clientes(None, None, None, None, None, None, None, None, None, None)
          TESTINSTANCE.Grabar(dfc)
          nombre_tabla="CLIENTES"
          nombre_output = f"{filepath_output}\\{nombre_tabla}_{fecha_actual}.txt" 
          dfc.to_csv(nombre_output,sep=';' ,index=False)
          print(f"Archivo procesado guardado como {nombre_output}")
          
     else : 
          print("Faltan columnas , se detiene el proceso.") 
          sys.exit() 
elif filepath_input.endswith('.xslx'):  
     
     #separador = detectar_separador(filepath_input) 
     fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
     dfc= pd.read_excel(filepath_input, sheet_name=0, engine='openpyxl',dtype='string')
     num_columnas = dfc.shape[1]  
     print ("Tiene la siguiente cant de columnas : ", num_columnas) 

     #dfc.info()
     ###TRANSFORMACION
     #VALIDACIÓN DE FORMATO DE COLUMNAS ADMITIDAS PARA EL PROCESO 


     print(dfc.head(100)) 
     print(dfc.info())
     if num_columnas == 10 :
          dfc= corregir_columnas_CLIENTES(dfc) 
          print(dfc.head(98))
          print("Todo ok") 
          TESTINSTANCE = Clientes(None, None, None, None, None, None, None, None, None, None)
          TESTINSTANCE.Grabar(dfc)
          nombre_tabla="CLIENTES"
          nombre_output = f"{filepath_output}\\{nombre_tabla}_{fecha_actual}.csv" 
          dfc.to_csv(nombre_output, index=False)
          print(f"Archivo procesado guardado como {nombre_output}")
          
     else : 
          print("Faltan columnas , se detiene el proceso.") 
          sys.exit() 
else : 
      print("Formato de archivo no permitido. /n")
      print("Los formatos permitidos son .txt, .csv y .xslx")
      sys.exit()
