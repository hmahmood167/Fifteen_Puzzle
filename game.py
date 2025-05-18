#author: Hafsah Mahmood
#date: 12/08/23
#GUI
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
import sys
#creates a list of button objects for the board
buttons = []
def clickButton(tiles, name):
    move = int(name)
    if tiles.is_valid_move(move):
        tiles.update(move)
        #setting the base case for index
        index_zero = -1
        index_move = -1
        for i in range(0, 16):
            button = buttons[i]
            text = str(button.cget('text'))
            if text == '':
                index_zero = i
            elif text == name:
                index_move = i
        #exit program in case of error
        if index_zero == -1 or index_move == -1:
            print('Sorry, internal error')
            sys.exit()
        #button variables
        zero_button = buttons[index_zero]
        move_button = buttons[index_move]
        buttons[index_move] = zero_button
        buttons[index_zero] = move_button
        #4x4 grid for the GUI
        for i in range(0, 4):
           for j in range(0, 4):
                buttons[i*4+j].grid(row=i+1, column=j)
        #restart game when done
        if tiles.is_solved():
            print('You solved it! Quit or quit and restart to play again.')


if __name__ == '__main__':
    #create game tiles
    tiles = Fifteen()
    tiles.shuffle()
    #create game window
    gui = Tk()
    gui.title("Fifteen")
    #create a font for GUI
    font = font.Font(family='Helveca', size='24', weight='bold')
    #creates buttons for game
    for i in range(0, 16):
        text = StringVar()
        if not tiles.tiles[i] == 0:
            text.set(tiles.tiles[i])
        else:
            text.set('')
        name = str(tiles.tiles[i])
        button = Button(gui, textvariable=text, name=name,
                        bg='white', fg='black', font=font, height=2, width=5,
                        command = lambda name=name: clickButton(tiles, name))
        #change the color
        if not tiles.tiles[i] == 0:
            gui.nametowidget(name).configure(bg='coral')
        #append button to list of buttons for GUI
        buttons.append(button)
    #create a 4x4 grid for the GUI
    for i in range(0, 4):
        for j in range(0, 4):
            buttons[i*4+j].grid(row=i+1, column=j)
    #update the window
    gui.mainloop()