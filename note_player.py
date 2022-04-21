from array import array
from time import sleep
from math import sin

from tkinter import *
from tkinter.simpledialog import *
import pygame
from pygame.mixer import Sound, get_init, pre_init

tk = Tk()
c = Canvas(tk, width=1000, height=160, bg="#ffffff")
c.pack()

class Note(Sound):
    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = 4 * int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

notemap = {
    0:103.826174, # Ab2
    1:116.54094, # Bb2
    2:130.812783, # C3
    3:155.563492, # Eb3
    4:174.614116, # F3
    5:207.652349, # Ab3
    6:233.081881, # Bb3
    7:261.625565, # C4
    8:311.126984, # Eb4
    9:349.228231, # F4
    10:415.304698, # Ab4
    256:None # Rest
    }

heightmap = {
    0:130, # Ab3
    1:125, # Bb3
    2:120, # C4
    3:110, # Eb4
    4:105, # F4
    5:60, # Ab4
    6:55, # Bb4
    7:50, # C5
    8:40, # Eb5
    9:35, # F5
    10:25, # Ab5
    }

tempo = 144

note_seq = []

def play_note(note_id, length):
    """Plays a note on an Ab pentatonic scale with a given
note id (0 = Ab1, 1 = Bb1, 2 = C2, etc.) and a given
length in beats"""
    if note_id != 256:
        note = Note(notemap[note_id])
        note.play(-1)
    sleep(length/(tempo/60)-(1/tempo))
    if note_id != 256:
        note.stop()
    sleep(1/tempo)

pre_init(44100, -16, 1, 1024)
pygame.init()

note_id_text = \
"""Note id
0 = Low Ab
1 = Low Bb
2 = Low C
3 = Low Eb
4 = Low F
5 = Middle Ab
6 = Middle Bb
7 = Middle C
8 = Middle Eb
9 = Middle F
10 = High Ab"""

class SoundControls():
    def play(event):
        for note in note_seq:
            play_note(note[0], note[1])
    def addrest(event):
        note_seq.append([256, askinteger(" ","Note length (beats)", minvalue=1, maxvalue=4)])
    def addnote(event):
        note_seq.append([askinteger(" ",note_id_text, minvalue=0, maxvalue=10), askinteger(" ","Note length (beats)", minvalue=1, maxvalue=4)])
    def subnote(event):
        note_seq.pop(len(note_seq)-1)

c.bind_all("<KeyPress-n>", SoundControls.addnote)
c.bind_all("<KeyPress-r>", SoundControls.addrest)
c.bind_all("<KeyPress-s>", SoundControls.subnote)
c.bind_all("<KeyPress-space>", SoundControls.play)

while True:
    c.delete("all")
    c.create_line(10, 30, 990, 30)
    c.create_line(10, 40, 990, 40)
    c.create_line(10, 50, 990, 50)
    c.create_line(10, 60, 990, 60)
    c.create_line(10, 70, 990, 70)
    c.create_line(10, 100, 990, 100)
    c.create_line(10, 110, 990, 110)
    c.create_line(10, 120, 990, 120)
    c.create_line(10, 130, 990, 130)
    c.create_line(10, 140, 990, 140)
    c.create_line(20, 110, 20, 105, 25, 100, 30, 105, 30, 120, 15, 135, width=1.5)
    c.create_line(35, 103, 35, 107, width=1.5)
    c.create_line(35, 113, 35, 117, width=1.5)
    c.create_line(20, 35, 25, 30, 30, 35, 30, 45, 15, 50, 30, 55, 30, 65, 25, 70, 20, 65, width=1.5)
    c.create_line(15, 30, 15, 70, width=1.5)
    c.create_rectangle(10, 30, 12, 70, fill="#000000")
    c.create_text(40, 55, text="♭")
    c.create_text(47, 40, text="♭")
    c.create_text(54, 60, text="♭")
    c.create_text(40, 125, text="♭")
    c.create_text(47, 110, text="♭")
    c.create_text(54, 130, text="♭")
    c.create_text(70, 40, text="4", font=("Default", 15))
    c.create_text(70, 60, text="4", font=("Default", 15))
    c.create_text(70, 110, text="4", font=("Default", 15))
    c.create_text(70, 130, text="4", font=("Default", 15))
    offset = 80
    for note in note_seq:
        if note[0] != 256:
            notey = heightmap[note[0]]
            nleng = note[1]
            if nleng == 4:
                c.create_oval(offset, notey+4, offset+10, notey-4, width=1.5)
            elif nleng == 2:
                c.create_oval(offset, notey+4, offset+10, notey-4, width=1.5)
                c.create_line(offset+10, notey, offset+10, notey-25, width=1.5)
            elif nleng == 3:
                c.create_oval(offset, notey+4, offset+10, notey-4, width=1.5)
                c.create_line(offset+10, notey, offset+10, notey-25, width=1.5)
                c.create_line(offset+13, notey-1, offset+13, notey+1, width=1.5)
            elif nleng == 1:
                c.create_oval(offset, notey+4, offset+10, notey-4, width=1.5, fill="#000000")
                c.create_line(offset+10, notey, offset+10, notey-25, width=1.5)
        elif note[0] == 256:
            nleng = note[1]
            if nleng == 4:
                c.create_rectangle(offset, 46, offset+10, 50, fill="#000000")
            elif nleng == 2:
                c.create_rectangle(offset, 54, offset+10, 50, fill="#000000")
            elif nleng == 3:
                c.create_rectangle(offset, 54, offset+10, 50, fill="#000000")
                c.create_line(offset+15, 49, offset+13, 51, width=1.5)
            elif nleng == 1:
                c.create_line(offset, 35, offset+5, 40, offset, 50, offset+5, 55, offset, 55, offset+3, 60, width=1.5)
        offset += 15
    tk.update()
