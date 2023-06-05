Isepp Rebane
06/01/2023
Foundations of Programming: Python (IT FDN 110 A Sp 23)
Assignment 07 – Files & Exceptions

Files & Exceptions
Introduction
At the time of writing this paper, I visited a website that claimed to have every file format type listed. The total was 292. It is a safe assumption that the total could be higher. Every file type, and it’s characteristics are unique This write up discusses writing to files and how to account for possible errors when you interact with files.
Read, Write, Append, Open, Save, Delete, Copy, Move, Find, Zip, Own
Hello.txt.  A simple text file, that has a text string “Hello World!” Simple enough right?
Think again…

What method do you use to read the data, write to a new or existing file, if you append a file-are the current values replaced, how do you open-make changes-then save the file, what happens in a program if you delete a file, are there copy and move protections, file is buried 27 directories deep in an EXT4 file system-how do you search for it, what takes place with the data when it’s compressed and decompressed, and most importantly, who owns it, and does that actually mean???

This assignment is ambiguous. There are no instructions as to what this week’s program should look like. When you interact with files, all bets are off. There is literally an endless number of possibilities of how a computer program can interact with them.
ERROR
There are program errors, and user errors. You have error messages for developers, and error messages for users. How do you around for them? Error handling.

try:
    new_file = input("Enter file name: ")
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
    print("There was a non-specific error!")

01000010:01101001:01101110:01100001:01110010:01111001
The above is the binary expression for the word-binary. Data can be saved in binary format instead of just "plain" text. In Python, this technique called pickling. Storing data in a binary format can obscure the file's content and may reduce the file's size.
Assignment
There were no formal directions for this week’s assignment, I assumed the script should interact with a binary file and error handing be present.
Code located here: https://github.com/Tricepp/IntroToProg-Python-Mod7

Line 1-9: File Header

Line 11: Import Pickle

Line 14: ToDo.dat variable declared

Line 16-84: I created my program in one class called main, and split all the actions into functions within the main class. As I was working with a .dat (data) file, I made a script that asks for a single task and priority. The read and write function both contain try and except for error handling.

Line 85-104: Main script in a while loop. I made my script look similar to assignment 06 with the separation of concerns.
Summery

•	Files, file formats, and the endless ways you can interact with them.
•	Error handling.
•	Binary and binary files.
•	An overview of this week’s assignment and my code.
