from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
  redurn "Hello World"
  
@app.route("/marco<polo>")
def marco(polo):
   return "%s" %polo 
