# --- IMPORT LIBRARIES
import os
import sys
import time
import shutil
import tkinter
from tkinter import filedialog
from tkinter import messagebox

# --- R_NAMING INSTRUCTIVE INFO
created_folder_name = "_R_NAMING_"
tool_title = "Batch Re_Naming Tool | Version 03.19 | Copyright © 2019 Zach X.G. Zheng | Zach@Zachitect.com | Zachitect.com"

# --- WARNING MESSAGE
warning_window_title = "IMPORTANT NOTICE!"
warning_existing_folder = f"{created_folder_name} folder already exists in this location, would you like to replace it?"
warning_empty_directory = "Please select a directory first!"
warning_integer_input = "Invalid Input! Please Enter an Interger!"
warning_preview = "Please preview names before renaming!"
warning_empty_existing = "Please select files to operate on first!"
warmomg_renaming_sure = "Proceed to Rename?"
message_finished = "Operation Finished"
warning_quit = "Would you like to cancel the session and quit?"
warning_quit_delete = f"Would you like to delete the {created_folder_name} folder and its content?"

# --- LONG TEXT CONTENT
R_Introduction = '''
1. Select a location to create a backup folder to safely operate on renaming files.
2. Select multiple files to rename and confirm selected file list in left window.
3. Compose new file names in the above format, preview names before renaming.

Composing  Example: Project Best  12345  +  1  Final Issue  .  pdf
Produced New Name: Project Best_12345_Final Issue.pdf
Produced New Name: Project Best_12346_Final Issue.pdf
'''

# --- DATA RECORDING PARAMETER
ls_selected_file_name = []
ls_new_file_name = []
ls_selected_file_path = []
ls_new_file_path = []
ls_int_component = []


# --- TKINTER GRAPHIC CONTROL
root_colour = "#2A363B"
cursor_type = "plus"

button_act_bg = "#2A363B"
button_act_fg = "#ffffff"
button_fg = "#ffffff"

button_borderwidth = 0
button_font = ("Helvetica", 11)
button_relief = "flat"

text_bg = "#3f4a4e"
text_fg = "#ffffff"
text_borderwidth = 0
text_cursor = "plus"
text_font = ("Helvetica", 10)
text_pad_LR = 2
text_pad_TD = 2
text_relif = "flat"

entry_fg = "#ffffff"
entry_hlc = "#2F9599"
entry_hlb = "#2F9599"
entry_hl_thickness = 5
entry_relief = "flat"

entry_borderwidth = 0
entry_font = ("Helvetica", 10)


# --- TKINTER GUI MAIN WINDOW
root = tkinter.Tk()
root.title(tool_title)
root.configure(bg = "#2F9599",cursor = cursor_type, bd = 5)
root.resizable(True, True)
root.overrideredirect(False)

for row in range(0,6):
    root.rowconfigure(row, weight=1)
for column in range(0,9):
    root.columnconfigure(column, weight=1)


# --- TKINTER GLOBAL DISPLAY VARIABLES
tkdefault = "Thisisanidentitytopreventmisoperations"

set_directory_string = tkinter.StringVar(value = tkdefault)
set_existing_name_string = tkinter.StringVar(value = tkdefault)
set_new_name_string = tkinter.StringVar(value = tkdefault)

input_prefix = tkinter.StringVar(value = "prefix")
input_integer = tkinter.StringVar(value = "integer")
input_changer = tkinter.StringVar(value = "integer")
input_suffix = tkinter.StringVar(value = "suffix")
input_extension = tkinter.StringVar(value = "extension")

# --- R_NAMING OPERATIONAL FUNCTIONS
def force_int(input):
    while True:
        if len(str(input)) == 0:
            return 0
        else:
            try:
                int(input)
            except ValueError:
                return tkdefault
            else:
                return int(input)

def tkpopup_choice(window_title, window_message):
    user_bool = messagebox.askokcancel(window_title, window_message)
    return user_bool


def tkupdate_text(tk_textbox, content):
    tk_textbox.config(state = "normal")
    tk_textbox.delete("1.0", "end")
    tk_textbox.insert("1.0", str(content))
    tk_textbox.config(state = "disabled")


def select_create_directory():
    selected_path = filedialog.askdirectory()
    if not len(selected_path) == 0:
        create_folder_path = selected_path + f"/{created_folder_name}"
        if not os.path.exists(create_folder_path):
            os.makedirs(create_folder_path)
            set_directory_string.set(create_folder_path)
            tkupdate_text(t_directory.object,create_folder_path)
        else:
            if tkpopup_choice(warning_window_title, warning_existing_folder) == True:
                shutil.rmtree(create_folder_path)
                os.makedirs(create_folder_path)
                set_directory_string.set(create_folder_path)
                tkupdate_text(t_directory.object,create_folder_path)
            else:
                pass
    else:
        tkupdate_text(t_directory.object,warning_empty_directory)


def select_operating_files():
    if not set_directory_string.get() == tkdefault:
        selected_file_path = filedialog.askopenfilenames()
        if not len(selected_file_path) == 0:
            ls_selected_file_name.clear()
            ls_selected_file_path.clear()
            for file in selected_file_path:
                ls_selected_file_path.append(file)
                ls_selected_file_name.append(os.path.basename(file))
                joined_string_existing_name = ('\n').join(ls_selected_file_name)
                set_existing_name_string.set(joined_string_existing_name)
                tkupdate_text(t_existing_names.object, joined_string_existing_name)
        else:
            pass
    else:
        tkupdate_text(t_directory.object,warning_empty_directory)

def build_name_integer():
    ls_new_file_name.clear()
    ls_new_file_path.clear()
    if not set_directory_string.get() == tkdefault:
        if not set_existing_name_string.get() == tkdefault:
            file_list_size = range(0, len(ls_selected_file_name))
            if not force_int(input_changer.get()) == tkdefault and not force_int(input_integer.get()) == tkdefault and int(input_changer.get()) > 0:
                ls_int_component.clear()
                if force_int(input_integer.get()) == 0 and len(str(input_integer.get())) == 0:
                    for i in file_list_size:
                        changer_output = str(int(input_changer.get()) * i)
                        ls_int_component.append(changer_output)
                    return True
                else:
                    for i in file_list_size:
                        temp_int = int(input_integer.get()) + int(input_changer.get()) * i
                        int_addition_digit = len(str(temp_int))
                        int_str_digit = len(str(input_integer.get()))
                        prefix_zero = "0" * (int_str_digit - int_addition_digit)
                        changer_output = prefix_zero + str(temp_int)
                        ls_int_component.append(changer_output)
                    return True
            else:
                tkupdate_text(t_new_names.object,warning_integer_input)
        else:
            tkupdate_text(t_existing_names.object,warning_empty_existing)
    else:
        tkupdate_text(t_directory.object,warning_empty_directory)

def build_name_compose():
    if build_name_integer() == True:
        file_list_size = range(0, len(ls_int_component))
        for i in file_list_size:
            composed_new_name = input_prefix.get() + str(ls_int_component[i]) + input_suffix.get() + "." + input_extension.get()
            ls_new_file_name.append(composed_new_name)
            ls_new_file_path.append(set_directory_string.get() +"/" + composed_new_name)
            joined_string_new_name = ('\n').join(ls_new_file_name)
            set_new_name_string.set(joined_string_new_name)
            tkupdate_text(t_new_names.object, joined_string_new_name)

def renaming_operation():
    if not set_directory_string.get() == tkdefault:
        if not set_existing_name_string.get() == tkdefault:
            if not set_new_name_string.get() == tkdefault:
                if tkpopup_choice(warning_window_title, warmomg_renaming_sure ) == True:
                    file_list_size = range(0, len(ls_selected_file_name))
                    for file_to_clean in os.listdir(set_directory_string.get()):
                        os.remove(set_directory_string.get() + '/' + file_to_clean)
                    for i in file_list_size:
                        shutil.copy(ls_selected_file_path[i], set_directory_string.get())
                        temp_copied_file_path = set_directory_string.get() + "/" + ls_selected_file_name [i]
                        os.rename(temp_copied_file_path, ls_new_file_path [i])
                        tkupdate_text(t_directory.object, message_finished)
                        os.startfile(set_directory_string.get())

                else:
                    pass
            else:
                tkupdate_text(t_new_names.object,warning_preview)
        else:
            tkupdate_text(t_existing_names.object,warning_empty_existing)
    else:
        tkupdate_text(t_directory.object,warning_empty_directory)


def quit_cancel():
    if tkpopup_choice(warning_window_title, warning_quit) == True:
        if set_directory_string.get() == tkdefault:
            root.destroy()
            sys.exit()
        else:
            if tkpopup_choice(warning_window_title, warning_quit_delete) == True:
                shutil.rmtree(set_directory_string.get())
                root.destroy()
                sys.exit()
            else:
                pass
    else:
        pass


help_condiiton = False
def help_hit():
    global help_condiiton
    if help_condiiton == False:
        help_condiiton = True
        frame_intro.object.grid(row = 6, column = 0, rowspan = 1, columnspan = 9)
        root.geometry("900x511")
    else:
        help_condiiton = False
        frame_intro.object.grid_forget()
        root.geometry("900x335")



# --- TKINTER CLASSES
class frame:
    def __init__(self, parent_frame, back_ground, frame_hl_thickness, frame_hl_bg,row_coordinate, column_coordinate, row_span, column_span):
        self.object = tkinter.Frame(parent_frame, bg = back_ground, bd = 0, cursor = cursor_type, relief = "flat", highlightbackground = frame_hl_bg, highlightthickness = frame_hl_thickness, highlightcolor = frame_hl_bg)
        self.object.grid(row = row_coordinate, column = column_coordinate, rowspan = row_span, columnspan = column_span, sticky = "news")
        for row in range(0, row_span):
            self.object.rowconfigure(row, weight = 1)
        for column in range(0, column_span):
            self.object.columnconfigure(column, weight = 1)
        self.object.grid_propagate(False)

class button:
    def __init__(self, parent_frame, button_bg, button_text, button_command, button_state, row_coordinate, column_coordinate, row_span, column_span):
        self.object = tkinter.Button(parent_frame, activebackground = button_act_bg, activeforeground = button_act_fg, text = button_text, bd = button_borderwidth, bg = button_bg, fg = button_fg, font = button_font, relief = button_relief, state = button_state, command = button_command)
        self.object.grid(row = row_coordinate, column = column_coordinate, rowspan = row_span, columnspan = column_span, sticky = "news")
        self.object.grid_propagate(False)

class display:
    def __init__(self, parent_frame, row_coordinate, column_coordinate, row_span, column_span):
        self.object = tkinter.Text(parent_frame, height = 10, width = 10, bg = text_bg, fg = text_fg, bd = text_borderwidth, cursor = text_cursor, font = text_font, padx = text_pad_LR, pady = text_pad_TD, relief = text_relif, state = "disabled")
        self.object.grid(row = row_coordinate, column = column_coordinate, rowspan = row_span, columnspan = column_span, sticky = "news")
        self.object.grid_propagate(False)

class entry:
    def __init__(self, parent_frame, entry_bg, entry_textvariable,row_coordinate, column_coordinate, row_span, column_span):
        self.object = tkinter.Entry(parent_frame, bg = entry_bg, fg = entry_fg, highlightcolor = entry_hlc, highlightbackground = entry_hlb, highlightthickness = entry_hl_thickness, relief = entry_relief, bd = entry_borderwidth, font = entry_font, textvariable = entry_textvariable, justify = "center")
        self.object.grid(row = row_coordinate, column = column_coordinate, rowspan = row_span, columnspan = column_span, sticky = "ew")
        self.object.grid_propagate(False)


# --- TKINTER FRAMES
frame_button = frame(root,"#2A363B",0, "#2A363B", 0,0,5,1)
frame_display_dir = frame(root,"#3f4a4e",0, root_colour, 0,1,1,8)
frame_display_name_frame = frame(root,"#2A363B",0, root_colour, 1,1,4,8)
frame_display_names = frame(frame_display_name_frame.object,"#2A363B",5, root_colour, 0,0,4,8)
frame_old = frame(frame_display_names.object,"#2A363B",0, "#2A363B", 0,0,4,4)
frame_new = frame(frame_display_names.object,"#2A363B",0, "#2A363B", 0,4,4,4)
frame_entry = frame(root,"#2F9599",0, "#ffffff", 5,1,1,8)
frame_empty = frame(root, "#2F9599",0, "#ffffff", 5,0,1,1)
frame_intro = frame(root,"#2F9599",0,"#2F9599", 6,0,1,9)
frame_intro_sub = tkinter.Frame(frame_intro.object)
frame_intro_sub.pack(side = "bottom")

# --- TKINTER SEPARATORS (USING FRAME WIDTH = 1)
frame_separator = tkinter.Frame(frame_display_names.object,bg = root_colour,bd = 1,height = 10, width = 0, relief = "flat")
frame_separator.pack(expand =1, fill = "y")


# --- TKINTER BUTTONS
b_select_directory = button(frame_button.object,"#F8B195" ,"Location",select_create_directory,"normal", 0,0,1,1)
b_select_files = button(frame_button.object,"#F67280" ,"Files",select_operating_files,"normal", 1,0,1,1)
b_preview = button(frame_button.object,"#C06C84" ,"Preview",build_name_compose,"normal", 2,0,1,1)
b_rename = button(frame_button.object,"#6C5B7B" ,"Rename",renaming_operation,"normal", 3,0,1,1)
b_cancel = button(frame_button.object,"#355C7D","Cancel",quit_cancel,"normal", 4,0,1,1)
b_help = button(frame_empty.object,"#2F9599","HELP!",help_hit,"normal", 0,0,1,1)


# --- TKINTER TEXT BOXES
t_directory = display(frame_display_dir.object, 0,0,1,8)
t_existing_names = display(frame_old.object, 0,0,4,4)
t_new_names = display(frame_new.object, 0,0,4,4)


# --- TKINTER INPUT ENTRIES
e_prefix = entry(frame_entry.object,"#3f4a4e",input_prefix, 0,0,1,1)
e_integer = entry(frame_entry.object,"#3f4a4e",input_integer, 0,1,1,1)
e_changer = entry(frame_entry.object,"#3f4a4e",input_changer, 0,3,1,1)
e_suffix = entry(frame_entry.object,"#3f4a4e",input_suffix, 0,4,1,1)
e_extension = entry(frame_entry.object,"#3f4a4e",input_extension, 0,6,1,1)


# --- TKINTER LABELS
plus_label = tkinter.Label(frame_entry.object, text = "✚", fg = "#ffffff",bg = "#2F9599",font=("Helvetica", 10))
ext_label = tkinter.Label(frame_entry.object, text = "●", fg = "#ffffff",bg = "#2F9599",font=("Helvetica", 10))
intro_label = tkinter.Label(frame_intro_sub, justify = "left", text = R_Introduction, height = 10, fg = "#ffffff",bg = "#2F9599",font = ("Helvetica", 11))

plus_label.grid(row = 0, column = 2, rowspan = 1, columnspan = 1, sticky = "ew")
ext_label.grid(row = 0, column = 5,rowspan = 1, columnspan = 1, sticky = "ew")
intro_label.pack()

# --- TKINTER MAINLOOP
frame_intro.object.grid_forget()
root.geometry("900x335")
root.mainloop()