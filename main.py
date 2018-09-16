from flask import Flask, request
from caesar import rotate_character
#check to make sure this is correct bc there is no rotate_string function in caesar

app = Flask (__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
  <head>
    <style>
      form {{
          background-color: #eee;
          padding:20px;
          margin: 0 auto;
          width: 540px:
          font: 16px sans-serif;
          boarder-radius: 10px;
      }}

      textarea {{
          margin:10px 0;
          width:540px;
          height: 120px
      }}
    </style>
  </head>

  <body>
    <form method ="post">
      <label> Rotate by:
      <input type="text" name="rot" />
      </label>
      <br>
    <textarea name="text">{0}</textarea> 
      <br>
      <input type="submit" />
    </form>  
  </body>
</html>
"""

@app.route("/")
def index():
    return form.format()

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form ['rot']
    rot = int(rot)
    text = request.form ['text']
    text = str(text)

    encrypted = ""
    for each_char in text:
        if each_char == '':
            encrypted = encrypted + ''
        else:
            each_char = rotate_character(each_char,rot)
            encrypted = encrypted + each_char

    return '<h1>'+form.format(encrypted)+'</h1>'  

app.run()   