from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


#@app.route('/')
#def landing_page():
#	return render_template('welcome.html', name='welcome')

@app.route('/play')

def play_page():
	return render_template('index.html', name='play')

@app.route('/status', methods=["GET", "POST"])
def get_game_status():
	is_running = request.args.get('game_status')
	return is_running

if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost', port=5000)