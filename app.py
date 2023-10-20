"""Madlibs Stories."""
from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'pugzy'
# debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template('index.html', prompts=prompts)

@app.route('/story')
def story_result():
    """ displays user's story"""

    text = story.generate(request.args)
    return render_template("story.html", text=text)
