from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = 'your-secret-key-1234'  # Change for production

@app.route('/')
def hello_name():
   return 'Hello Word' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,threaded=True, debug=True)