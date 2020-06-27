from flask import Flask, render_template, url_for

def flask_app():
    app = Flask(__name__)

    @app.route('/')
    def my_home():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0')
