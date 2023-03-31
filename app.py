from flask import Flask 

app=Flask(__name__)


@app.route('/')
def index():
    return '<h1>welcome by Dhivya</h1>'git 
if __name__=='__main__':
    app.run(debug=True) 
