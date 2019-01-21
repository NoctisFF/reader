# -*- coding: utf-8 -*-

import os, time
import Tkinter as tk
from Tkinter import *

def sentence_display():
    sentence = []
    f = open('test.txt', 'rb')
    text = f.read()
    par = text.split('\r\n')
    for i in par:
        par_sent = i.split('.')
        for j in range(len(par_sent)):
            sentence.append(par_sent[j])
    for i in range(sentence.count('')):
        sentence.remove('')
    return sentence

class Text(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self._count = 0
        self._divider = 2
        self._stages_count = 0
        self._words_counter = 0
        self._stage_words = []

    def sentence_lenght(self):
        self._words = sentence_display()[self._count].split(' ')
        self._length = len(self._words)

        #if self._length / self._divider <= 7:
        try:
            for i in range(self._words_counter, self._words_counter + 3):
                self._stage_words.append(self._words[i])
        except IndexError:
            # for i in range(self._words_counter, self._length):
            #     self._stage_words.append(self._words[i])
            pass
        else:
            self._divider += 1

        self.config(text=self._stage_words)
        if self._stages_count < int(self._length / self._divider):
            self._stages_count += 1
            self._words_counter += 3
            del self._stage_words[:]
        if self._stages_count > int(self._length / self._divider) - 1:
            self._count += 1
            self._stages_count = 0
            self._divider = 2
            self._words_counter = 0
            del self._stage_words[:]
        self.after(1000, self.sentence_lenght)



    def text_to_dispay(self):
        self.config(text=sentence_display()[self._count])
        if self._count < len(sentence_display())-1:
            self._count += 1
        self.after(300, self.text_to_dispay)

window = tk.Tk()

counter = Text(window)
counter.pack()
counter.sentence_lenght()

# label = Text(window)
# label.pack(padx=25, pady=50)
# label.text_to_dispay()

mainloop()



