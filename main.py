from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="style.css">
        
           
    </head>
    <body>
      <!-- create your form here -->
        <form action="/" method="post">
            <label for="Rotate by">Rotate by:</label>
            <input type="text" name="rot" value ="0" />
            <textarea name="text">{0}</textarea>
            <input type="submit" value="submit" />
            
        </form>
                

    </body>
</html>
"""

@app.route("/")
def index():
    
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    encrypted_string = rotate_string(text, rot)
    
    return form.format(encrypted_string)


app.run()