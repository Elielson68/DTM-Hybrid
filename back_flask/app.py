from flask import Flask, Response, render_template
from flask_socketio import SocketIO
from tool import DTM


def create_app():
    app = Flask(__name__)
    dtm = DTM()
    dtm.init_app(app)
    socketio = SocketIO(app, cors_allowed_origins="*")
    
    @app.route("/")
    def home():
        return Response(app.dtm.Run(), mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route("/measurement")
    def measurement():
        return {"value": app.dtm.measurement}

    return app

