from flask import Flask, render_template, request
from flask import send_file #biblioteca o modulo send_file para forzar la descarga
import uuid  #Modulo de python para crear un string

#Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename 
#El módulo os en Python proporciona los detalles y la funcionalidad del sistema operativo.
import os 
from os import remove #Modulo  para remover archivo
from os import path #Modulo para obtener la ruta o directorio


#Declarando nombre de la aplicación e inicializando
app = Flask(__name__)

  
  
#Funcion que recorre todos los archivos almacenados en la carpeta (archivos)  
def listaArchivos():
    urlFiles = 'static/archivos'
    return (os.listdir(urlFiles))

     
#Creando un Decorador
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', list_Photos = listaArchivos())


@app.route('/guardar-foto', methods=['GET', 'POST'])
def registarArchivo():
        if request.method == 'POST':
            if(request.files['archivo']):
                #Script para archivo
                file     = request.files['archivo']
                basepath = path.dirname (__file__) #La ruta donde se encuentra el archivo actual
                filename = secure_filename(file.filename) #Nombre original del archivo
                
                #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
                extension           = path.splitext(filename)[1]
                nuevoNombreFile     = uuid.uuid4().hex + extension
        
                upload_path = path.join (basepath, 'static/archivos', nuevoNombreFile) 
                file.save(upload_path)
        return render_template('index.html', list_Photos = listaArchivos())
    

@app.route('/<string:nombreFoto>', methods=['GET','POST'])
def EliminarFoto(nombreFoto=''):
    if request.method == 'GET':
        #print(nombreFoto) #Nombre del archivo subido
        basepath = path.dirname (__file__) #C:\xampp\htdocs\elmininar-archivos-con-Python-y-Flask\app
        url_File = path.join (basepath, 'static/archivos', nombreFoto)
        #print(url_File)
        
        #verifcando si existe el archivo, con la funcion (path.exists) antes de de llamar remove 
        # para eliminarlo, con el fin de evitar un error si no existe.
        if path.exists(url_File):
            remove(url_File) #Borrar foto desde la carpeta
            #os.unlink(url_File) #Otra forma de borrar archivos en una carpeta
    return render_template('index.html', list_Photos = listaArchivos())
        
    

@app.route('/descargar/<string:nombreFoto>', methods=['GET','POST'])
def descargar_Archivo(nombreFoto=''):
    basepath = path.dirname (__file__) 
    url_File = path.join (basepath, 'static/archivos', nombreFoto)
    #send_file toma 2 parametros, el primero será la ruta del archivo y el
    # 2 será as_attachment=True porque deseamos que el archivo sea descargable.
    resp =  send_file(url_File, as_attachment=True)
    return resp    
    
    
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return 'Ruta no encontrada'


#Arrancando la aplicacion
if __name__ == '__main__':
    app.run(debug=True, port=5000)