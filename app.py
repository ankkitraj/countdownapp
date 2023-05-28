from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('countdown.html')

@app.route('/countdown', methods=['GET'])
def countdown():
    deadline = datetime.strptime(request.args.get('deadline'), '%Y-%m-%dT%H:%M')
    now = datetime.now()
    time_left = deadline - now
    countdown_values = {
        'Days': time_left.days,
        'Hours': time_left.seconds // 3600,
        'Minutes': (time_left.seconds // 60) % 60,
        'Seconds': time_left.seconds % 60
    }
    return jsonify(countdown_values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
