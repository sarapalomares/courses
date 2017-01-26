from flask import Flask, render_template #render_template allows us to render the files in the template folder

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name="Sara")

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True) #this means we're going to run our application and we're going to run it in debug mode. If there are any errors, it will show up in the browser
