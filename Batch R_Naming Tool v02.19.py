import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# Fixed Parameters -----
Tool_Name = 'BATCH RE-NAMING TOOL'
created_folder_name = "_R_Naming_"
warning_1 = "Important Notice"
warning_1_content = "R_Naming folder already exists in this location (Ignorable)"
warning_integer = "Invalid Input! Please Enter an Interger!"
warning_preview = "Please preview names before renaming!"
R_instruction = """
1. Select a location to create a folder
2. Select files to back up and then rename
3. Rename selected files into new names
4. Hopefully it does what it is made for
"""
Entry_Instruction = """
Please fill the above blanks with info of new filenames in the following format
Prefix and suffix can be empty, must enter integer and extension name
-----------------------------------------------------------------------------------------------------------------------------
PREFIX  -  START INTEGER  ✚  CHANGING INTEGER  -  SUFFIX  ●  EXTENSION NAME
-----------------------------------------------------------------------------------------------------------------------------
Filename Example: [Project Best_]  [12345] + [1]  [Final Issue] . [pdf]
Produced New Name: Project Best_12345_Final Issue.pdf
Produced New Name: Project Best_12346_Final Issue.pdf
Produced New Name: Project Best_12347_Final Issue.pdf

-----------------------------------------------------------------------------------------------------------------------------
Version 02.19 | Copyright © 2019 Zach X.G. Zheng | zach@zachitect.com | zachitect.com
"""
# Data Recording Parameter -----
copied_file_list = []
copied_file_list_short = []
new_file_list = []
new_file_list_short = []


# GUI Main Window -----
main_window = tk.Tk()
main_window.title(Tool_Name)
main_window.geometry("780x960")

frame_instruction = Frame(main_window, bg = "#222222")
frame_directory  = Frame(main_window, bg = "#222222")
frame_files_display = Frame(main_window, bg = "#222222")
frame_file_old = Frame(frame_files_display, bg = "#222222")
frame_file_new = Frame(frame_files_display, bg = "#222222")
frame_entries = Frame(main_window, bg = "#222222")

#miruku_logo = tk.PhotoImage(file = "‎⁨/Users/Zach⁩/⁨Dropbox⁩/⁨Permanent Content/0.⁩")

# GUI Main Configure -----
main_window.configure(bg='#222222')

# global parameters -----
set_directory = tk.StringVar(value = "All selected files will be copied here...")
set_files = tk.StringVar(value = "Files to be renamed...")
new_files = tk.StringVar(value = "New filenames set...")

input_prefix = tk.StringVar(value = "prefix")
input_integer = tk.StringVar(value = "integer")
input_changer = tk.StringVar(value = "integer")
input_suffix = tk.StringVar(value = "suffix")
input_extension = tk.StringVar(value = "extension")

# operation functions -----

def insert_Text(TkinterText,TextContent):
    TkinterText.config(state = NORMAL)
    TkinterText.delete('1.0', END)
    TkinterText.insert('1.0',str(TextContent))
    TkinterText.config(state = DISABLED)


def select_directory_button():
    select_directory = filedialog.askdirectory()
    created_folder_path = select_directory + f'/{created_folder_name}'
    if not len(select_directory) == 0:
        set_directory.set(created_folder_path)
        print(created_folder_path)
    if not os.path.exists(created_folder_path):
        os.makedirs(created_folder_path)
        insert_Text(text_display_directory,created_folder_path)
    else:
        messagebox.showwarning(warning_1,warning_1_content)
        insert_Text(text_display_directory,created_folder_path)


def select_files_to_copy():
    selected_files = filedialog.askopenfilenames()
    destination = set_directory.get()
    copied_file_list.clear()
    copied_file_list_short.clear()
    if not destination == "All selected files will be copied here...":
        for selected_file in selected_files:
            copied_file_list.append(selected_file)
            copied_file_list_short.append(os.path.basename(selected_file))
            joined_copied_file_list = ('\n').join(copied_file_list_short)
            set_files.set(joined_copied_file_list)
            insert_Text(text_display_files, joined_copied_file_list)
    else:
        insert_Text(text_display_directory, "Please select a directory first...")

def new_file_names():
    new_prefix = input_prefix.get()
    new_integer = input_integer.get()
    new_changer = input_changer.get()
    new_suffix = input_suffix.get()
    new_extension = input_extension.get()
    new_file_list.clear()
    new_file_list_short.clear()
    # -----
    file_list_size = len(copied_file_list)
    if not file_list_size == 0 and not Force_Integer(new_integer) == warning_integer and not Force_Integer(new_changer) == warning_integer:
        file_index = range(0,file_list_size)
        for i in file_index:
            index_integer = int(new_integer) + int(new_changer) * i
            new_name_short = new_prefix + str(index_integer) + new_suffix + "." + new_extension
            new_name_full = set_directory.get() +'/' + new_name_short
            new_file_list_short.append(new_name_short)
            new_file_list.append(new_name_full)
            join_new_file_list_short = ('\n').join(new_file_list_short)
            insert_Text(text_display_newname, join_new_file_list_short)
    else:
        insert_Text(text_display_newname, warning_integer)


def renaming_number_sequence():
    destination = set_directory.get()
    new_prefix = input_prefix.get()
    new_integer = input_integer.get()
    new_changer = input_changer.get()
    new_suffix = input_suffix.get()
    new_extension = input_extension.get()
    # -----
    file_list_size = len(copied_file_list)
    if not file_list_size == 0 and not Force_Integer(new_integer) == warning_integer and not Force_Integer(new_changer) == warning_integer and text_display_newname.get('1.0','end') == ('\n').join(new_file_list_short)+'\n':
        if messagebox.askokcancel(warning_1,"Proceed to Rename?") == True:
            file_index = range(0,file_list_size)
            for file_to_clean in os.listdir(destination):
                os.remove(destination + '/' +file_to_clean)
            for i in file_index:
                old_name_single = copied_file_list[i]
                new_name_single = new_file_list[i]
                shutil.copy(old_name_single, destination)
                copy_temp_files = destination + "/" + os.path.basename(old_name_single)
                os.rename(copy_temp_files,new_name_single)
                insert_Text(text_display_directory, "OPERATION FINISHED")
                os.startfile(set_directory.get())
        else:
            print("cancelled")
    else:
        insert_Text(text_display_newname, warning_preview)


def Cancel_quit():
    destination = set_directory.get()
    if not destination == "All selected files will be copied here...":
        if messagebox.askokcancel(warning_1,"Quit and Delete The Folder Created and its Contents") == True:
            shutil.rmtree(set_directory.get())
            sys.exit()
        else:
            print("Not Quit Not Delete")
    else:
        sys.exit()


def Force_Integer(input):
    while True:
        try:
            int(input)
        except ValueError:
            return warning_integer
            continue
        else:
            return int(input)
            break

# GUI functions -----
# Run Application -----

# GUI Module -----
Label_Title = tk.Label(frame_instruction, justify = LEFT, relief = FLAT, fg = "#888888", bg = '#222222', text = 'B A T C H    R E - N A M I N G    T O O L' , font=('IMPACT', 20))
Label_instruction = tk.Label(frame_instruction, justify = LEFT, relief = FLAT, fg = "#888888", bg = '#222222', text = R_instruction , font=('Helvetica', 12))


Label_old = tk.Label(frame_file_old, justify = LEFT, relief = FLAT, fg = "#888888", bg = '#222222', text = 'CURRENT NAMES' , font=('Helvetica', 12))
Label_new = tk.Label(frame_file_new, justify = LEFT, relief = FLAT, fg = "#888888", bg = '#222222', text = 'NEW NAMES' , font=('Helvetica', 12))

Label_Digit_Plus = tk.Label(frame_entries, justify = LEFT, relief = FLAT, fg = "#888888", bg = '#222222', text = "✚", font=('Helvetica', 12))
Label_Extension_Dot = tk.Label(frame_entries, justify = LEFT, relief = FLAT, fg = "#888888", bg = '#222222', text = "●", font=('Helvetica', 12))

Label_Entry_Instruction = tk.Label(frame_entries, justify = LEFT, relief = FLAT, fg = "#888888", bg = '#222222', text = Entry_Instruction , font=('Helvetica', 12))



select_directory_button = tk.Button(frame_directory, width = 20, highlightbackground = "#222222", bg = "#222222", fg = "#999999", text = 'Create Folder', font=('Helvetica', 12), command = select_directory_button)
select_files_button = tk.Button(frame_directory, width = 20, highlightbackground = "#222222", bg = "#222222", fg = "#999999", text = 'Select Files', font=('Helvetica', 12), command = select_files_to_copy)
button_update_new_name = tk.Button(frame_entries, width = 20, highlightbackground = "#222222", bg = "#222222", fg = "#999999", text = 'Preview', font=('Helvetica', 12), command = new_file_names)
button_rename = tk.Button(frame_entries, width = 20, highlightbackground = "#222222", bg = "#222222", fg = "#999999", text = 'Rename', font=('Helvetica', 12), command = renaming_number_sequence)
button_quit = tk.Button(frame_entries, width = 20, highlightbackground = "#222222", bg = "#222222", fg = "#999999", text = 'Cancel', font=('Helvetica', 12), command = Cancel_quit)

text_display_directory = tk.Text(frame_directory, width = 92, height = 1, bg = "#dddddd", highlightbackground = "#222222", highlightthickness = 3)
text_display_directory.config(state = DISABLED)

text_display_files = tk.Text(frame_file_old, width = 45, height = 15, bg = "#dddddd", highlightbackground = "#222222", highlightthickness = 6)
text_display_files.config(state = DISABLED)

text_display_newname = tk.Text(frame_file_new, width = 45, height = 15, bg = "#dddddd", highlightbackground = "#222222", highlightthickness = 6)
text_display_newname.config(state = DISABLED)

entry_0 = tk.Entry(frame_entries, textvariable = input_prefix, width = 15, bg = "#dddddd", highlightbackground = "#222222", highlightthickness = 6, bd = 0, highlightcolor = "#000000", font=('Helvetica', 15), justify = CENTER)
entry_1 = tk.Entry(frame_entries, textvariable = input_integer, width = 10, bg = "#007f9f", highlightbackground = "#222222", highlightthickness = 6, bd = 0, highlightcolor = "#000000", font=('Helvetica', 15), justify = CENTER)
entry_2 = tk.Entry(frame_entries, textvariable = input_changer, width = 10, bg = "#007f9f", highlightbackground = "#222222", highlightthickness = 6, bd = 0, highlightcolor = "#000000", font=('Helvetica', 15), justify = CENTER)
entry_3 = tk.Entry(frame_entries, textvariable = input_suffix, width = 15, bg = "#dddddd", highlightbackground = "#222222", highlightthickness = 6, bd = 0, highlightcolor = "#000000", font=('Helvetica', 15), justify = CENTER)
entry_4 = tk.Entry(frame_entries, textvariable = input_extension, width = 10, bg = "#dddddd", highlightbackground = "#222222", highlightthickness = 6, bd = 0, highlightcolor = "#000000", font=('Helvetica', 15), justify = CENTER)


# GUI Frame Pack -----
Label_Title.pack(side = "top")
Label_instruction.pack(side = "top")
Label_old.pack(side = "bottom")
Label_new.pack(side = "bottom")

select_directory_button.pack(side = "top")
text_display_directory.pack(side = "top")
select_files_button.pack(side = "top")

text_display_files.pack(side = "top")
text_display_newname.pack(side = "top")

Label_Entry_Instruction.pack(side = "bottom")
button_update_new_name.pack(side = "top")
button_rename.pack(side = "top")
button_quit.pack(side = "top")

entry_0.pack(side = "left")
entry_1.pack(side = "left")
Label_Digit_Plus.pack(side = "left")
entry_2.pack(side = "left")
entry_3.pack(side = "left")
Label_Extension_Dot.pack(side = "left")
entry_4.pack(side = "left")

# GUI SUB MAIN ------
frame_file_old.pack(side = "left")
frame_file_new.pack(side = "right")

# GUI Main Loop
frame_instruction.pack()
frame_directory.pack()
frame_files_display.pack()
frame_entries.pack()



main_window.mainloop()
