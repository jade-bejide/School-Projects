#To do:
#need to save fonts and colours to saved file

from guizero import *

app = App(title="Wordy!")


# function for reading files
def open_file():
    with open(file_name.value, "r") as f:
        editor.value = f.read()

# function for writing files
def save_file():
    with open(file_name.value, "w") as f:
        f.write(editor.value)

    #save_button.disable()
    save_button.hide()

def enable_save():
    #save_button.enable()
    save_button.show()

def disableName():
    if file_name.value == "":
        open_button.disable()
        save_button.disable()
    else:
        open_button.enable()
        save_button.enable()

def increaseSize():
    editor.text_size += 1

def decreaseSize():
    editor.text_size -= 1

def change_fontBlack():
    editor.text_color = "black"

def change_fontNavy():
    editor.text_color = "navy"

def change_fontCyan():
    editor.text_color = "cyan"

def change_fontPink():
    editor.text_color = "deep pink"


def times():
    editor.font = "times new roman"

def arial():
    editor.font = "arial"
def yesQuit():
    app.destroy()

def noQuit():
    save_file()
    app.destroy()
    
def exit_app():
    if save_button.enabled == True:
        window = Window(app, height=140, width=450)
        warning = Text(window, text="Are you sure you want to exit without saving the file")

        yes = PushButton(window, command=yesQuit, text="Yes", align="left")
        no = PushButton(window,command=noQuit, text="Save File", align="right")
        yes.resize(4,1)
        no.resize(4,1)

def light():
    app.bg = "white"
    file_controls.bg ="LightSteelBlue1"
    menubar.bg = "white"

def dark():
    app.bg = "gray"
    file_controls.bg ="dark slate gray"
    menubar.bg = "lightgrey"
    
    
        
# create a box to house the controls, we want the box to span the entire width of the app
file_controls = Box(app, align="top", width="fill")

file_controls.bg ="LightSteelBlue1"



# create a TextBox for the file name
file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left", command=disableName)
menubar = MenuBar(app, toplevel=["File", "Edit", "Font Colour", "Font Size", "Font", "Toggle Light Mode"], options=[
                   
                      [ ["Exit", exit_app], ["Open", open_file]],
                      [ ["Save", save_file]],
                      [["Black", change_fontBlack], ["Navy", change_fontNavy], ["Cyan", change_fontCyan], ["Deep pink", change_fontPink]],
                      [["Increase Size", increaseSize], ["Decrease Size", decreaseSize]],
                      [["Times New Roman", times], ["Arial", arial]],
                      [["Light", light], ["Dark", dark]]
                  ])

# create a save button which uses the save_file function
save_button = PushButton(file_controls, text="Save", command=save_file, align="right")

save_button.resize(2, 1)

# create an open button which uses the open_file function
open_button = PushButton(file_controls, text="Open", command=open_file,  align="right")

open_button.resize(2, 1)

# create a TextBox which is not in the box and fills the rest of the GUI
editor = TextBox(app, multiline=True, height="fill", width="fill", command=enable_save)

app.display()
