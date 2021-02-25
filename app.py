from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Cloud4c</title>
   
<style>
    h3
        {
            color:blue;
        }
    #s
    {
            height:50px;
            width: 1200px;
    }
   
</style>
</head>
<body>
    <div style="background-color:hsl(241, 88%, 51%)" id='s'>
        <h1 style='color:white;'> Cloud4c </h1>
    </div>
   
    <h3>Welcome to Cloud4C !! CICD Automation with Google Cloud Native Tools !!</h3>
   
</body>
</html>
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
