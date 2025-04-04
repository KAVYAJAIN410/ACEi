from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Route to serve the control page (for laptop)
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve the VR page (for mobile)
@app.route('/vr')
def vr():
    return render_template('vr.html')

# Event to handle key press messages (from the laptop)
@socketio.on('move_object')
def handle_key_press(data):
    direction = data.get('direction')
    print(f"Key press received: {direction}")  # Debugging
    emit('move_object', data, broadcast=True)

# Event to handle distance setting
@socketio.on('set_distance')
def handle_set_distance(data):
    distance = data.get('distance')
    print(f"Distance set to: {distance}px")  # Debugging
    emit('set_distance', {'distance': distance}, broadcast=True)
    
@socketio.on('remove')
def handle_remove(data):
    freq = data.get('Frequency')
    emit('remove', {'freq':freq}, broadcast=True)

@socketio.on('slide1')
def handle_slide1():
    emit('slide1', broadcast=True)

@socketio.on('slide2')
def handle_slide2():
    emit('slide2', broadcast=True)
    
@socketio.on('slide3')
def handle_slide3():
    emit('slide3', broadcast=True)

# Run the app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
