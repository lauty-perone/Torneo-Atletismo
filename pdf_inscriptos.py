import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Ruta a la carpeta principal que contiene tus carpetas con archivos CSV
ruta_carpeta_principal = '/Users/lauty/Desktop/AtletismoUnlp/'
archivos_csv = [os.path.join(ruta, archivo) for ruta, _, archivos in os.walk(ruta_carpeta_principal) 
                for archivo in archivos if archivo.endswith('.csv')]
with PdfPages('Inscriptos Torneo Ciudad de La Plata.pdf') as pdf:
    # os.walk() devuelve la ruta de la carpeta, las carpetas dentro de esa carpeta y los archivos en esa carpeta
        for archivo in archivos_csv:
            if archivo.endswith('.csv'):
                # Asegúrate de usar la ruta completa al archivo CSV
                ruta_archivo = os.path.join(ruta_carpeta_principal, archivo)
                nombre_archivo = os.path.splitext(os.path.basename(archivo))[0]

                df = pd.read_csv(ruta_archivo)
                fig, ax =plt.subplots(figsize=(12,4))
                ax.axis('tight')
                ax.axis('off')
                tabla = ax.table(cellText=df.values,
                                 colLabels=df.columns,
                                 cellLoc = 'center', 
                                 loc='center')

                # Cambiar el color de fondo de las celdas
                cells = tabla.properties()["children"]
                for cell in cells:
                    cell.set_facecolor("#F4F6F7")  # Puedes cambiar el color aquí

                # Cambiar el tamaño de la fuente
                tabla.auto_set_font_size(False)
                tabla.set_fontsize(6)  # Puedes cambiar el tamaño de la fuente aquí

                plt.title(nombre_archivo)  # Aquí cambiamos el título
                pdf.savefig(fig, bbox_inches='tight')

