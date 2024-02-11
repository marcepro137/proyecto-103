import os
import shutil

from_dir = "C:/Users/homer/Downloads"
to_dir = "C:/Users/homer/OneDrive/Desktop"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name, extencion = os.path.splitext(i)
    if extencion == "":
        continue
    if extencion in ['.txt', '.doc', '.docx', '.pdf']:
        ruta1 = from_dir+'/'+i
        ruta2 = to_dir+'/'+"Archivos_Documentos"
        ruta3 = to_dir+'/'+"Archivos_Documentos"+'/'+i
        if  os.path.exists(ruta2):
            print("Moviendo " + i + "...")

            shutil.move(ruta1, ruta3)

        
        else:
            os.makedirs(ruta2)
            print("Moviendo " + i + "...")

            shutil.move(ruta1, ruta3)
