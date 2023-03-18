import tkinter as tk
import os
from tkinter import font as tkFont

root = tk.Tk()
frame = tk.Frame(root)
root.geometry("600x200+100+50")
helv36 = tkFont.Font(family='Helvetica', size=11, weight='bold')

class Entry:
    def __init__(self, entryNum, ans, root_title, root):
        self.entryNum = entryNum
        self.ans = ans
        self.root_title = root_title
        self.root = root

    def enter(self, result, runNum, ans):
        result = result.get()
        if runNum == 1:
            global path
            path = result
            ans.config(text=f"Your path is: {path}")
            entry1.destroy()
            enter_button.destroy()
            part2.input2()
        elif runNum == 2:
            global amount
            amount = int(result)
            ans.config(text=f"Your number of files is: {amount}")
            entry2.destroy()
            enter_button.destroy()
            part3.input3()

        elif runNum == 3:
            global old_name
            old_name = result
            ans.config(text=f"Your old file name is: {old_name}")
            entry3.destroy()
            enter_button.destroy()
            part4.input4()
            
        elif runNum == 4:
            global new_name
            new_name = result
            ans.config(text=f"The new file name is: {new_name}(numbers).png")
            entry4.destroy()
            enter_button.destroy()
            renaimgmg = tk.Label(text="Renaming files...").pack()
            part4.change_names(path,amount,old_name,new_name)
            done = tk.Label(text="Done!").pack()
        
        
    def input1(self):
        global entry1, enter_button
        root.title(self.root_title)
        ans1 = tk.Label(root, text="")
        entry1 = tk.Entry(root, width=45)
        ans1.pack(side="top")
        entry1.pack()
        enter_button = tk.Button(root, text="enter", command=lambda:part1.enter(entry1,1,ans1),font=helv36)
        enter_button.pack()

    def input2(self):
        global entry2, enter_button
        root.title(self.root_title)
        ans2 = tk.Label(root, text="")
        entry2 = tk.Entry(root, width=45)
        ans2.pack(side="top")
        entry2.pack()
        enter_button = tk.Button(root, text="enter", command=lambda:part2.enter(entry2,2,ans2),font=helv36)
        enter_button.pack()

    def input3(self):
        global entry3, enter_button
        root.title(self.root_title)
        ans3 = tk.Label(root, text="")
        entry3 = tk.Entry(root, width=45)
        ans3.pack(side="top")
        entry3.pack()
        enter_button = tk.Button(root, text="enter", command=lambda:part3.enter(entry3,3,ans3),font=helv36)
        enter_button.pack()

    def input4(self):
        global entry4, enter_button
        root.title(self.root_title)
        ans4 = tk.Label(root, text="")
        entry4 = tk.Entry(root, width=45)
        ans4.pack(side="top")
        entry4.pack()
        enter_button = tk.Button(root, text="enter", command=lambda:part4.enter(entry4,4,ans4),font=helv36)
        enter_button.pack()

    def change_names(self, path, amount, old_name, new_name):
        x = 0
        for i in range(amount):
            ol_name = fr"{path}\{old_name}"+" "+f"({x+1})"+".png"
            ne_name = fr"{path}\{new_name}"+f"{x}"+".png"

            # Renaming the file
            os.rename(ol_name, ne_name)
            x += 1

part1 = Entry(1,1,"What is you file path?",root)
part2 = Entry(2,2,"How many files do you want to rename?",root)
part3 = Entry(3,3,"What is the name of the OLD file?(Don't say file extension)",root)
part4 = Entry(4,4,"What is the new name you want?",root)

top = tk.Toplevel()
top.geometry("1000x450+800+50")
top.title("Instructions")
l2 = tk.Label(top, text = '''Instructions:
1.  Most important is to follow the prompts that appear in the window title, the name to the left of the Minus, Fullscreen and Close button.

2.  This is also very important, when you are putting your file path on the first input, don’t have any speech marks, as this messes up the code.
Do not include the name of the image in the file path, only the folders.

3.  You have to sort of set up the file in order to be named, to do this, ctrl + a all of the images in file explorer,
and rename them. The images should have the names ‘file (1), file (2)’ and so on.
If you scroll to the last image, that number at the end is the amount of files you have,
so that would be one of the inputs.

Limitation:
This code was designed for the sole purpose of renaming files for bakkesmods’ alphaconsole plugin for making animated decals.
If you wanted something different to batch rename files, unfortunately, this is not for you.
I have not made inputs give errors and let you do it again, so if you input wrong and the program closes without doing anything, you will have to run it again.
Limited to pngs

Notes:
This code is very simple, but helps majorly when making the animated decals as it writes the names in the formatting you would want for the animated decals
This also means if it doesn’t work, it is normally just a bad input. If the problem persists, DM Ethnogeny#1409 on Discord.
No input is meant to have a file extension name in it, so only do the name you want, the file extension is automatically set
''').pack()

part1.input1()

root.mainloop()
