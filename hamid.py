from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def test():
    return render_template('index.html')

if _name_ == '_main_':
    app.run()
