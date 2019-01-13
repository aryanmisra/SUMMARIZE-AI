#!/usr/bin/env python

from __future__ import print_function

import pandas as pd
from keras_text_summarization.library.seq2seq import Seq2SeqSummarizer
import numpy as np

np.random.seed(42)
data_dir_path = 'demo/data' # refers to the demo/data folder
model_dir_path = 'demo/models' # refers to the demo/models folder
def main(X):
    #df = pd.read_csv(data_dir_path + "/fake_or_real_news.csv")
    #X = df['text']
    #Y = df.title
    Y = "fill"
    #Y = "A very brave new Canadian: Woman who fled Saudi Arabia arrives in Toronto"
    config = np.load(Seq2SeqSummarizer.get_config_file_path(model_dir_path=model_dir_path)).item()
    summarizer = Seq2SeqSummarizer(config)
    summarizer.load_weights(weight_file_path=Seq2SeqSummarizer.get_weight_file_path(model_dir_path=model_dir_path))

    x = X
    actual_headline = Y
    headline = summarizer.summarize(x)
    return headline

data = input("hi: ")
print(data)
pred = main(data)
print(pred)
"""

import sys
if __name__ == "__main__":
    f = open('README.txt', 'w')
    f.truncate()
    f.write('hello world')
    f.close()"""