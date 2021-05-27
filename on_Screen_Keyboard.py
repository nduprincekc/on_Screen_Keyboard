from tkinter import *
import ttkthemes
from tkinter import ttk
import webbrowser

def select(value):
    if value == 'Space':
        textarea.insert(INSERT, ' ')
    elif value == 'Tab':
        textarea.insert(INSERT, '\t')

    elif value == 'Enter':
        textarea.insert(INSERT, '\n')

    elif value == 'Del':
        textarea.delete(1.0, END)

    elif value == 'Backs':
        i = textarea.get(1.0, END)
        newText = i[:-2]
        textarea.delete(1.0, END)
        textarea.insert(INSERT, newText)

        # code for left shift key

    elif value == 'Shift ↑':
        leftShiftButtons = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Backs', 'Del',
                            'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', ']', '7', '8', '9',
                            'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', 'Enter', '4', '5', '6',
                            'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?', '↑ Shift down', '1', '2', '3',
                            'Space', 'hackers keyboard'
                            ]
        varRow = 2
        varColumn = 0

        for button in leftShiftButtons:
            command = lambda x=button: select(x)
            if button != 'Space':
                ttk.Button(root, text=button, width=5, command=command).grid(row=varRow, column=varColumn)
            else:
                ttk.Button(root, text=button, width=30, command=command).grid(row=6, column=0, columnspan=15)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1





    elif value == '↑ Shift down':
        varRow = 2
        varColumn = 0
        buttons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
                   'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '7', '8', '9',
                   'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
                   'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '↑ Shift down', '1', '2', '3',
                   'Space', 'hackers keyboard']

        for button in buttons:
            command = lambda x=button: select(x)

            if button != 'Space':
                ttk.Button(root, text=button, width=5, command=command).grid(row=varRow, column=varColumn)
            else:
                ttk.Button(root, text=button, width=30, command=command).grid(row=6, column=0, columnspan=15)
            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1

    elif value == 'hackers keyboard':


        ttk.Style().configure(root, padding=6, relief="flat",
                              background="#008000")

        # creating a global variable for the buttons
        varRow = 2
        varColumn = 0

        # buttons that will appear when  hackers keyboard is being clicked
        buttons = ['`', 'kali', 'facebook', 'tutorial', 'metaspolit', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
                   'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', '7', '8', '9',
                   'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'Enter', '4', '5', '6',
                   'Shift ↑', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', '↑ Shift', '1', '2', '3',
                   'Space']

        for button in buttons:
            command = lambda x=button: select(x)

            # arrangemnt of buttons in the keyboard
            if button != 'Space':
                ttk.Button(root, text=button, width=5,command=command).grid(row=varRow, column=varColumn)

            else:
                ttk.Button(root, text=button, width=30, command=command).grid(row=6, column=0, columnspan=15)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1



    elif value == 'Caps':
        varRow = 2
        varColumn = 0
        buttons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
                   'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', '7', '8', '9',
                   'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'Enter', '4', '5', '6',
                   'Shift ↑', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', '↑ Shift', '1', '2', '3',
                   'Space']

        for button in buttons:
            command = lambda x=button: select(x)

            if button == 'hackers keyboard':
                ttk.Style().configure(root, padding=6, relief="flat",
                                      background="#008000")
            elif button != 'Space':
                ttk.Button(root, text=button, width=5, command=command).grid(row=varRow, column=varColumn)
            else:
                ttk.Button(root, text=button, width=30, command=command).grid(row=6, column=0, columnspan=15)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1


    elif value == 'CAPS':
        varRow = 2
        varColumn = 0
        buttons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
                   'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '7', '8', '9',
                   'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
                   'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '↑ Shift down', '1', '2', '3',
                   'Space', 'hackers keyboard']

        for button in buttons:
            command = lambda x=button: select(x)
            if button != 'Space':
                ttk.Button(root, text=button, width=5, command=command).grid(row=varRow, column=varColumn)
            else:
                ttk.Button(root, text=button, width=30, command=command).grid(row=6, column=0, columnspan=15)
            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1

    # else insert the the key button
    else:
        textarea.insert(INSERT, value)

    # focus the cursor to the textarea
    textarea.focus_set()


root = ttkthemes.ThemedTk()
root.title('On Screen Keyboard')
root.resizable(0, 0)
root.get_themes()
root.set_theme('radiance')

# code for title label
titleLabel = Label(root, text='On Screen Keyboard', font=('arial', 20, 'bold'))
titleLabel.grid(row=0, column=0, columnspan=15)

textarea = Text(root, font=('arial', 15, 'bold'), height=10, width=100, bd=9)
textarea.grid(row=0, column=0, columnspan=15)
textarea.focus_set()

varRow = 2
varColumn = 0
buttons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
           'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '7', '8', '9',
           'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
           'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '↑ Shift down', '1', '2', '3',
           'Space', 'hackers keyboard']

for button in buttons:
    command = lambda x=button: select(x)
    if button != 'Space':
        ttk.Button(root, text=button, width=5, command=command).grid(row=varRow, column=varColumn)
    else:
        ttk.Button(root, text=button, width=30, command=command).grid(row=6, column=0, columnspan=15)

    varColumn += 1
    if varColumn > 14:
        varColumn = 0
        varRow += 1

root.mainloop()
