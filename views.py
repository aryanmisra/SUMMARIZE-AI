from __future__ import print_function
from flask import render_template
from flask import Flask, request
from flask_cors import CORS, cross_origin
import sqlite3
import click
from flask.cli import with_appcontext
import json
import sys
import pandas as pd
from keras_text_summarization.library.seq2seq import Seq2SeqSummarizer
import numpy as np

def main(X):
    Y = "fill"
    print(X)
    config = np.load(Seq2SeqSummarizer.get_config_file_path(model_dir_path=model_dir_path)).item()
    summarizer = Seq2SeqSummarizer(config)
    summarizer.load_weights(weight_file_path=Seq2SeqSummarizer.get_weight_file_path(model_dir_path=model_dir_path))
    print("summarizered")
    x = X
    headline = summarizer.summarize(x)
    return headline

np.random.seed(42)
data_dir_path = 'demo/data' # refers to the demo/data folder
model_dir_path = 'demo/models' # refers to the demo/models folder
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "123"

@app.route('/form', methods=['POST'])
@cross_origin(origin='*')
def form():
	data = request.get_json(silent=True)
	text_data = data["text"]
	print(text_data)
	Y = "fill"
	print(Y)
	config = np.load(Seq2SeqSummarizer.get_config_file_path(model_dir_path=model_dir_path)).item()
	summarizer = Seq2SeqSummarizer(config)
	summarizer.load_weights(weight_file_path=Seq2SeqSummarizer.get_weight_file_path(model_dir_path=model_dir_path))
	print("summarizered")
	x = text_data
	headline = summarizer.summarize(x)
	print(headline)
	f = open('README.txt', 'w')
	f.truncate()
	f.write(headline)
	f.close()


if __name__ == '__main__':
    app.run(debug=True)