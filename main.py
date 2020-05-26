from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

R_HOST = os.environ.get('REDIS_HOST')
R_PORT = os.environ.get('REDIS_PORT')
R_DB = os.environ.get('REDIS_DB')
R_PASSWORD = os.environ.get('REDIS_PASSWORD')

#connect to redis
rd = redis.Redis(host=R_HOST, port=R_PORT, db=R_DB, decode_responses=True)

#connect via TLS - preferred but need to setup the tls
#rds = redis.Redis( url='rediss://:password@hostname:port/0',
#    password='password',
#    ssl_keyfile='path_to_keyfile',
#    ssl_certfile='path_to_certfile',
#    ssl_cert_reqs='required',
#    ssl_ca_certs='path_to_ca_certfile')

@app.route('/')
def index():
	return show_landing()

def show_landing():
	rd.incr('counterKEY')
	visitor = rd.get('counterKEY')
	return render_template('index.html', result=visitor, content_type='application/json')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
