import eventlet
import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap
import sqlite3
import datetime
from threading import Lock



eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'test.mosquitto.org'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLEAN_SESSION'] = True

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

mqtt = Mqtt(app)
async_mode = None
socketio = SocketIO(app)
# thread = None
# thread_lock = Lock()

bootstrap = Bootstrap(app)

# Database


def dict_database(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect(':memory:')
conn.row_factory = dict_database
# #conn = sqlite3.connect('fastoryDB.db')

#  cursor
c = conn.cursor()


def create_database():
    c.execute("""CREATE TABLE IF NOT EXISTS Temperature (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 value integer
                 );""")
    print("Database created")

# insert into database


def insert_db(temp_value):
    print("Inserting into database")
    value = 10
    try:
        c.execute("INSERT INTO Temperature VALUES (:id,:value)",
              {'id': None, 'value': temp_value})
    except:
        print("Failed to insert in database")

#READ
def get_temp():
    #c.execute("SELECT * FROM robot WHERE brand=:brand", {'brand': brand})
    sqlSt="SELECT * FROM Temperature"
    c.execute(sqlSt)
    return c.fetchall()

temp = 20

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['GET'])
def getState():
    global temp
    # print("Retrieving data from database")
    # if(not get_temp()):
    #     return "database is empty"
    # else:
    temp +=1
    return str(temp)

if __name__ == '__main__':
    print("Starting server")
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=False)