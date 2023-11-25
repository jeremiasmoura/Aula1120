#app.py
from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello():
  return 'Hello, S3!'

if _name_ =='_main_':
   app.run(debug=True)
