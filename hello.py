from flask import Flask

app = Flask("My Hello World Application")

@app.route("/")
def hello():
    return "Hello World!"



#this checks if this is the main programm and it's not imported as a sudmodule 

if __name__=="__main__":
    app.run(debug=True)
# When no port is specified, starts at default port 5000