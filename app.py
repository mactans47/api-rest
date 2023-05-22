from flask import Flask, jsonify, request, render_template

import psycopg2

app = Flask(__name__)

from users import users

try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456',
        database = 'Prueba',
        port = '5432'
    )
    print('succesfull conexion')
except Exception as ex:
    print(ex)

connection.autocommit = True

@app.route('/estado')
def getEstado():
    return jsonify({'nameSystem': 'api-users', 'version': '0.0.1', 'developer':'Marco Antonio Canedo Rejas',
'email': 'mactans47@gmail.com'})

#listar un usuario en especifico por GET de un conjunto JSON
@app.route('/users/<string:user_ci>')
def getuser(user_ci):
    usersFound = [user for user in users if user['ci'] == user_ci]
    if(len(usersFound) > 0):
        return jsonify({'user': usersFound[0]})
    return jsonify({'message': 'user no found'})

#crear usuarios por POST
@app.route('/users', methods=['POST'])
def addusers():
    new_user = {
        'name': request.form['name'],
        'edad': request.form['edad'],
        'primer_apel': request.form['primer_apel'],
        'seg_apel': request.form['seg_apel'],
        'ci': request.form['ci'],
        'fec_nac': request.form['fec_nac']
    }
    con = connection.cursor()
    query = "INSERT INTO users(ci,nombre,primer_apel,seg_apel,fec_nac,edad) values('"+new_user['ci']+"','"+new_user['name']+"','"+new_user['primer_apel']+"','"+new_user['seg_apel']+"','2000-05-12',"+new_user['edad']+")"
    try:
        con.execute(query)
        print("El registro se completo")
    except Exception as ex:
        print(ex)
    con.close()
    return jsonify({"message": "Registro realizado"})

#listar datos de usuario por GET
@app.route('/users')
def listDataUsers():    

    con = connection.cursor()
    query = "SELECT * FROM users;"
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)
    data = con.fetchall()
    
    con.close()

    return jsonify(data)

#actualizar datos de usuario por PUT
@app.route('/users/<string:id_user>', methods=['PUT'])#, methods=['PUT'])
def updateDataUser(id_user):    

    con = connection.cursor()
    
    #muestra el registro antes de actualizar
    query = "SELECT * FROM users where id_user = " + id_user+";"
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)
    data = con.fetchall()
    
    #ejecuta la actualizacion
    query = "UPDATE users set ci = '0000000', nombre = 'nombredeprueba', primer_apel = 'primerapellido', edad = 100 where id_user = " + id_user+";"
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)

    #muestra registro despues de la actualizacion
    query = "SELECT * FROM users where id_user = " + id_user+";"
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)
    data2 = con.fetchall()    
        
    con.close()

    return jsonify({"Registro antes de la actualizacion": data}, {"Resgistro despues de la actualizacion": data2})

#eliminar un usuario por DELETE
@app.route('/users/<string:id_user>', methods=['DELETE'])
def deleteDataUser(id_user):
    con = connection.cursor()
    
    #muestra el registro antes de actualizar
    query = "SELECT * FROM users;"
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)
    data = con.fetchall()
    
    #ejecuta la actualizacion
    query = "DELETE FROM users where id_user = " + id_user+";"
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)

    #muestra registro despues de la actualizacion
    query = "SELECT * FROM users;"
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)
    data2 = con.fetchall()    
        
    con.close()

    return jsonify({"Registros antes de la eliminacion": data}, {"Registros despues de la eliminacion": data2})

#promedio por GET
@app.route('/users/promedio-edad')
def calcAVG():
    
    con = connection.cursor()

    query = "SELECT AVG(EXTRACT(YEAR FROM AGE(NOW(), fec_nac))) AS promedio_edades FROM users;"
    
    try:
        con.execute(query)
    except Exception as ex:
        print(ex)
    data = con.fetchall()
    
    return jsonify({'promedioEdad': data})

#http://localhost:4000
if __name__ == '__main__':
    app.run(debug=True, port=4000)
