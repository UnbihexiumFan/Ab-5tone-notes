# Ab Pentatonic Note Player

## Introduction
A python program that can play notes on the Ab pentatonic scale that I've been working on for the past two days

## Requirements
* _Pygame 2.1.2_
* _Python 3.10_

## Controls
n- create new note

    Note ID: Specifies which note id to use. Can be from 0-10, though rests use the id 256.
    Note length: Specifies the note length, in beats.

r- create new rest

    Note length: Specifies the note length, in beats.

s- remove note

    Removes the last note or rest in the track.

space- play

    Plays the track.

p- preset

	Plays a song from a predefined list.

arrow keys- move page

	Changes the page on the screen; if the amount of notes in your track is greater than 54, move to the next/previous set of 54 notes.

## Further Development
I really think this is more of a basic program, so I'll probably only put basic features in here, but there's also anoter note player I'm working on.
