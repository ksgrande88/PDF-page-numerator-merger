PDF-page-numberer-merger
Number PDF, Merge PDF, Timestamp PDF, Code Python
Small program that is able to quickly number PDFs on a folder in sequence, with partial page number from each PDF, and timestamps it.
The program is written in Python and compiled on Windows, so only Windows users may find use for the .exe version.
The program is quite small and easy-to-use, but it felt necessary to have it, because I couldn't find any software immediately available. 
There are online features such as iLovePDF that do these kinds of work on PDF files, but in order to achieve automation, customization and to make my FIRST PROJECT, I gave it a go.
The main help I can provide to anyone interested in using it is to translate the words from Portuguese to English, here it goes:
Arquivo = File
Abrir = Open
Fechar = Close
Sobre = About
Licença = Licence
Escolha da pasta = Choose folder
Escolher pasta = same
Numerar = Number
Qual o número da 1a página = What is the number of the 1st page? (in case you do not want to start on 1)
Unir PDF = Merge PDF
Unir todos PDF da pasta = Merge all PDF on folder

How it works from the user perspective:
The user must set a folder with only PDF files;
The files must be in the order that they will be numbered. Suggestion: 1.first_file.pdf, 2.second_file.pdf, 2.1. first_attach_second_file.pdf, 3.third_file.pdf and so on;
The user chooses this folder by clicking on the button ESCOLHER PASTA ;
In this folder a subfolder called NUMERADOS will be created;
In this subfolder all the files from the parent folder will have their copies numbered, the ORIGINAL FILES WILL NOT BE CHANGED;
The user will be able to merge the numbered files by clicking on UNIR PDF.

How it works from the developer perspective (useful if adaptations are needed):
The program requires path modules such as os, io, shutil, time, datetime;
The PyPDF2 library is used to parse and merge pages;
The fpdf library is used to write new data on the existing pages (I spent too much time trying to find one library that did both, without success);
Actually, fpdf creates a blank page with the desired text, further explanation follows below;
The natsorted library is used to sort the order from the files in the folder;
Tkinter library is used for the GUI.

Explanation of the code:
Tkinter is initiated with a StringVar for showing the path of the folder;
Every function is within the class App;
The screen, frames and layout are initiated;
The browse function asks for the directory and sets the global StringVar as the path;
The about and licence functions are pop-ups;
The frames are set up;
The layout menus are set up and the buttons are connected to the functions.
