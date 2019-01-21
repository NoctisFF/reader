import tkinter as tk
from tkinter import *
from tkinter import font

def sentence_display():
    sentence = []
    f = open('test.txt', 'r', encoding='utf-8')
    text = f.read()
    text = text[1:]
    par = text.split('\n')
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
        self._lenght = len(self._words)
        try:
            self.config(text=self._words[self._words_counter])
        except IndexError:
            pass
        if self._words_counter < len(self._words) - 1:
            self._words_counter += 1
        else:
            self._count += 1
            self._words_counter = 0
        if len(self._words[self._words_counter]) <= 4:
            self.after(300, self.sentence_lenght)
        elif len(self._words[self._words_counter]) > 4 and len(self._words[self._words_counter]) <= 7:
            self.after(400, self.sentence_lenght)
        elif len(self._words[self._words_counter]) >= 8:
            self.after(500, self.sentence_lenght)

    def text_to_dispay(self):
        self.config(text=sentence_display()[self._count])
        if self._count < len(sentence_display())-1:
            self._count += 1
        self.after(300, self.text_to_dispay)

window = tk.Tk()
window.config(height=350, width=500, background='black')

canvas = tk.Canvas(window)
canvas.pack(fill=BOTH, expand=5)
canvas.config(background='black')
canvas.create_line(50,100,150,100, fill='orange')
canvas.create_line(230,100,330,100, fill='orange')
canvas.create_line(150,100,150,90, fill='orange')
canvas.create_line(230,100,230,90, fill='orange')
canvas.create_line(50,170,150,170, fill='orange')
canvas.create_line(230,170,330,170, fill='orange')
canvas.create_line(150,170,150,180, fill='orange')
canvas.create_line(230,170,230,180, fill='orange')

verd = font.Font(family="Trebuchet MS", size=36, weight="bold")

counter = Text(window, font=verd)
counter.config(foreground='orange', background='black', height=1, padx=400)
counter.place(relx=0.5, rely=0.5, anchor=CENTER)
counter.sentence_lenght()

mainloop()
