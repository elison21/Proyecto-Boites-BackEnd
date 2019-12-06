from flask import Flask, jsonify,request
import mysql.connector

app = Flask(__name__)

bd = mysql.connector.connect(host='localhost', user ='alumno',
                             passwd= '12345',
                             database='proyecto')

cursor = bd.cursor()

@app.route('/Contactos/',methods = ["GET","POST"])
def Contactos():
    if request.method == "GET":
        contacts = []
        query = "SELECT * FROM contact"
        cursor.execute(query)
        for contacto in cursor.fetchall():
            d = {
                'id': contacto[0],
                'avatar': contacto[1],
                'nombre': contacto[2],
                'correo': contacto[3],
                'telefono': contacto[4],
                'facebook': contacto[5],
                'instagram': contacto[6],
                'twitter': contacto[7]
            }
            contacts.append(d)
            #
        print(contacts)
        return jsonify(contacts)
    else:
        data = request.get_json()
        print(data)

        query = "INSERT INTO contacto (nombre, correo, telefono, facebook, instagram, twitter) VALUES (%s, %s, %s, %s, %s, %s)"

        cursor.execute(query, (data['nombre'],
                               data['correo'],
                               data['telefono'],
                               data['facebook'],
                               data['instagram'],
                               data['twitter']))
        bd.commit()

        if cursor.rowcount:
            return jsonify({'data': 'Ok'})
        else:
            return jsonify({'data': 'Error'})

app.run(debug=True)