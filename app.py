from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
debug = DebugToolbarExtension(app)

@app.route('/')
def display_form():
    return render_template('/form.html')

@app.route('/story')
def display_story():
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adjective = request.args['adjective']
    plural = request.args['plural']
    print(request.args)
    return render_template('/story.html', place=place, noun=noun, verb=verb, adjective=adjective, plural=plural)