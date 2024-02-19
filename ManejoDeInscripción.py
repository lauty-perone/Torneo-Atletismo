import os
import pandas as pd

def guardar_pruebas_de_campo(df,nombre):
    #guarda el archivo de una prueba de campo en la carpeta "Pruebas de campo"
    df = df [["Nombre Apellido", "Fecha de Nacimiento", "Club"]]
    path_completo = os.path.join('Pruebas de campo', nombre)
    if (len(df) != 0 ):
        
        df.to_csv(path_completo,index= False)

def ordenar_serie(df):
    
    # Crear una nueva columna para las filas
    df['Andanivel'] = 0

    # Asignar las filas según el orden especificado
    orden_filas = [3, 4, 2, 5, 1, 6]
    num_atletas = len(df)
    num_filas = len(orden_filas)

    # Asignar a cada atleta a una fila basándose en su tiempo
    for i in range(num_atletas):
        # El índice en orden_filas es el resto de la división i / num_filas
        indice = i % num_filas
        df.iloc[i, df.columns.get_loc('Andanivel')] = orden_filas[indice]

    # Ordenar el DataFrame por la columna de fila
    df = df.sort_values('Andanivel')
    return df

def series(df,parametro,tamanio_filas = 6):
    #Recibe las pruebas de velocidad y hace la serie guardando cada serie en la carpeta correspondiente
    if (not os.path.exists(parametro)):
        os.makedirs(parametro)

    filas_divididas = [df[i:i + tamanio_filas] for i in range(0, len(df), tamanio_filas)] 

    for i, df_split in enumerate(filas_divididas):
        #df_split = df_split.sample(frac=1, random_state=42)
        nombre = (f'Serie {i + 1} {parametro}.csv')
        path_completo = os.path.join(parametro,nombre)
        if ('100' in parametro or '400' in parametro or '80' in parametro or '600' in parametro):
            df_split = ordenar_serie(df_split)
            df_split = df_split[["Andanivel","Nombre Apellido","Fecha de Nacimiento","Club","Marca"]]
        else:    
            df_split = df_split[["Nombre Apellido","Fecha de Nacimiento","Club","Marca"]]
        df_split.to_csv(path_completo, index=False)


#"Marca temporal","Nombre","Apellido",
# "Fecha de Nacimiento","Federación/ Asociación/Club","Seleccione género",
# "Apto Médico","80 Metros","600 Metros","100 Metros","400 Metros","1500 Metros",
# "3000 Metros","Pruebas de campo","Comprobante pago"  
          
def filtrar_80Metros(archivo):
    datos = archivo[archivo["80 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',"600 Metros",
        'Apto Médico',"100 Metros", '400 Metros', '1500 Metros', '3000 Metros'
        ,'Pruebas de campo',"Comprobante pago"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by="80 Metros", ascending =True)
    datos.rename(columns= {'80 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_600Metros(archivo):
    datos = archivo[archivo["600 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',"80 Metros",
        'Apto Médico',"100 Metros", '400 Metros', '1500 Metros', '3000 Metros',
        'Pruebas de campo',"Comprobante pago"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by= "600 Metros", ascending=True)
    datos.rename(columns= {'600 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_100Metros(archivo):
    datos = archivo[archivo["100 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '400 Metros', '1500 Metros', '3000 Metros'
        ,'Pruebas de campo',"Comprobante pago","80 Metros","600 Metros"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by="100 Metros", ascending =True)
    datos.rename(columns= {'100 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_400Metros(archivo):
    datos = archivo[archivo["400 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        'Pruebas de campo',"Comprobante pago","80 Metros","600 Metros"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by= "400 Metros", ascending=True)
    datos.rename(columns= {'400 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_1500Metros(archivo):
    datos = archivo[archivo["1500 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '400 Metros', '3000 Metros',
        'Pruebas de campo',"Comprobante pago","80 Metros","600 Metros"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos.rename(columns= {'1500 Metros': 'Marca'},inplace=True)
    datos = datos.sort_values(by= "Marca",ascending=True)
    return datos

def filtrar_3000Metros(archivo):
    datos = archivo[archivo["3000 Metros"] != None]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '400 Metros',
        'Pruebas de campo',"Comprobante pago","80 Metros","600 Metros"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    datos = datos.sort_values(by= "3000 Metros",ascending=True)
    datos.rename(columns= {'3000 Metros': 'Marca'},inplace=True)
    return datos

def filtrar_largo(archivo):
    archivo["Pruebas de campo"] = archivo["Pruebas de campo"].fillna("")
    datos = archivo[archivo["Pruebas de campo"].str.contains("LARGO", case=False)]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros','Pruebas de campo',"Comprobante pago","80 Metros","600 Metros"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    return datos

def filtrar_jabalina(archivo):
    datos = archivo[archivo["Pruebas de campo"].str.contains('JABALINA')]
    columnas_borrar = ['Marca temporal', 'Seleccione su género',
        'Apto Médico', '100 Metros', '1500 Metros', '3000 Metros',
        '400 Metros','Pruebas de campo',"Comprobante pago","80 Metros","600 Metros"]
    datos = datos.drop(columnas_borrar,axis=1)
    datos = datos.dropna()
    return datos

path_files = os.path.dirname(os.path.realpath("."))
patch_arch = os.path.join(path_files)
inscriptos = open(os.path.join(patch_arch,"AtletismoUnlp", "Torneo _Ciudad de La Plata_.csv"),'r',
                   encoding='utf8')
data_set = pd.read_csv(inscriptos, encoding='utf8')
data_set.rename(columns= {'Federación/ Asociación/Club': 'Club'},inplace=True)
''''''
#Inscriptos en data_set
data_set ["Nombre Apellido"] = data_set["Nombre"] + " "+data_set["Apellido"]
data_set =data_set.drop(["Nombre", "Apellido"],axis=1)

masculino = data_set[data_set["Seleccione su género"]== "Masculino"]
femenino = data_set[data_set["Seleccione su género"]== "Femenino"]

#PRUEBAS DE PISTA
series(filtrar_80Metros(masculino),"80 Metros Masculino U16",4)
series(filtrar_80Metros(femenino),"80 Metros Femenino U16")

series(filtrar_600Metros(masculino),"600 Metros Masculino U16")
series(filtrar_600Metros(femenino),"600 Metros Femenino U16")

series(filtrar_100Metros(masculino),"100 Metros Masculino U18 y Mayores",5)
series(filtrar_100Metros(femenino),"100 Metros Femenino U18 y Mayores",4)

series(filtrar_400Metros(masculino),"400 Metros Masculino U18 y Mayores",4)
series(filtrar_400Metros(femenino),"400 Metros Femenino U18 y Mayores")

series(filtrar_1500Metros(masculino),"1500 Metros Masculino U18 y Mayores",9)
series(filtrar_1500Metros(femenino),"1500 Metros Femenino U18 y Mayores",12)

series(filtrar_3000Metros(masculino),"3000 Metros Masculino U18 y Mayores",10)
series(filtrar_3000Metros(femenino),"3000 Metros Femenino U18 y Mayores",12)# el num dice la cant de competidores


#PRUEBAS DE CAMPO
if (not os.path.exists('Pruebas de campo')):
        os.makedirs('Pruebas de campo')
    
guardar_pruebas_de_campo(filtrar_largo(masculino),'Inscriptos Largo Masculino Ambas categorias.csv')
guardar_pruebas_de_campo(filtrar_largo(femenino),'Inscriptos Largo Femenino Ambas categorias.csv')

guardar_pruebas_de_campo(filtrar_jabalina(masculino),'Inscriptos Jabalina Masculino Ambas categorias.csv')
guardar_pruebas_de_campo(filtrar_jabalina(femenino),'Inscriptos Jabalina Femenino Ambas categorias.csv')


