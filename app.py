from flask import Flask
app=Flask(__name__)
@app.route('/')
def her():
  return "you are goddamn right!!!"
if __name__=='__main__':
  app.run(host='0.0.0.0',port=8080)

