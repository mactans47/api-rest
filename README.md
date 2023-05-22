LA API ESTA CREADA CON PYTHON Y FLASK, POR LO QUE DE INICIO SE INSTALA LA LIBRERIA FLASK.
> pip install flask

Para la permitir la conexion con Postgres se instala el drive correspondiente para Python:
> pip install psycopg2 

Correr la api desde: http://localhost:4000/user en el navegador.
Desde esta dirección raiz correr las demas rutas segun la descripción del ejercicio.

Para la prueba de la api en relacion a las rutas de PUT y DELETE se utilizo para el envio de datos la aplicacion INSOMNIA, el cual permite probar diferentes tipos de envio por HTTP, sin necesidad de incorporar una interfaz explícita. Ver capturas de los resultados en la carpeta img.

El archivo form.html se constituye en un formulario de prueba para la ruta de creacion de nuevos registros de usuario, los cuales son almacenados en la base de datos Prueba de postgres, en la tabla "users"

El archivo comprimido "env" contiene los archivos de entorno de la aplicacion, en el se encuentra la referencia a flask, psycopg2, entre otros. 