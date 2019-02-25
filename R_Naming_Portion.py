import os
import shutil
from tkinter import filedialog

print("INSTRUCTION! MUST READ!")
print(" " * 10)
print("=" * 10)
print(" " * 10)
print("THIS TOOL WILL MAKE COPY OF YOUR ORIGINAL FILES AND RENAME THEM,")
print("I WILL FIRST ASK YOU TO SELECT A LOCATION TO PUT YOUR RENAMED FILES,")
print("AND THEN ASK YOU TO SELECT THE FILES YOU WOULD LIKE TO RENAME,")
print("SELECTED FILES WILL BE ORDERED ALPHABETICALLY REGARDLESS THE SEQUENCE OF SELECTION")
print(" " * 10)
print("=" * 10)
print(" " * 10)
print()

def PROCEED():
    inp = input("Please input Y to proceed, or N to cancel:\n")
    if inp == "Y":
        print("")
    elif inp == "N":
        quit()
    else:
        print("Invalid Input! Try Again!")
        PROCEED()
PROCEED()



# ask user to select a location for creating the renaming folder
dir = filedialog.askdirectory()

# create renaming folder
folder = "R_Naming"
c_dir = (dir + f"/{folder}")

if not os.path.exists(c_dir):
    os.makedirs(c_dir)

# copy files over to the new folder
ex_files = filedialog.askopenfilenames()

c_files = []
for ex_file in ex_files:
    c_file = shutil.copy(ex_file,c_dir)
    c_files.append(c_file)


def YESORNO():
    inp = input("Input Y to Continue, Or N to Cancel:\n")
    if inp == "Y":
        print("")
    elif inp == "N":
        shutil.rmtree(c_dir)
        quit()
    else:
        print("Invalid Input! Try Again!")
        YESORNO()


# new file names
length = len(ex_files)
len_index = range(0,length)

#------------------------

c_name_len = len(c_dir) + 1
c_pure_names = []
print ("Your are about to rename the following files:")
for c_file in c_files:
    c_pure_name = c_file[c_name_len:]
    c_pure_names.append(c_pure_name)
    print (c_pure_name)

YESORNO()

#------
print("""Copy or Type the portion of the existing name
on left of the part to be kept:""")
input_before_keep = input()
input_keep = input("Copy or Type the portion to keep:\n")
lbk = len(input_before_keep)
ltk = len(input_keep)
ppks = []
for ppp in c_pure_names:
    ppk = str(ppp)[lbk:ltk + lbk]
    ppks.append(ppk)

#------
nam0 = str(input("Input Name Before 'KEEP':\n"))
nam2 = str(input("Input Name After 'KEEP':\n"))
ext = str(input("Input Extension Name WITH Dot:\n"))

namset = []
for lindex in len_index:
    new_keep = ppks[lindex]
    new_name = nam0 + new_keep + nam2 + ext
    namset.append(new_name)
#------

print ("Your Files Will be Renamed into the Following:")
for nnn in namset:
    print (nnn)

YESORNO()

# renaming
for lindex in len_index:
    new_full_name = c_dir + f"/{namset[lindex]}"
    ex_full_name = c_files[lindex]
    os.rename(ex_full_name,new_full_name)
print("Your files have been renamed. Enjoy :)")

os.startfile(c_dir)
