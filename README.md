PDF-page-numerator-merger
Small  program that is able to quickly numerate PDFs on a folder on sequence, with partial from each PDF and timestamps it
The program is written in Python and compiled on Windows, so only Windows users may find use on the .exe version.
The program is quite small and easy, but it felt necessary due to me not being able to find any ready one on a more-than-quick search
There are online features as iLovePDF that do these kinds of work on PDF, but in order to achieve automation, customization and to be my FIRST PROJECT, I gave it a go.

The main help I can provide to anyone interested on using it is to translate the words from Portuguese to English, here it goes:
Arquivo = File
Abrir = Open
Fechar = Close
Sobre = About
Licença = Licence
Escolha da pasta = Choose folder
Escolher pasta = same
Numerar = Numerate
Qual o número da 1a página = What is the number of the 1st page? (in case you don't want to start on 1)
Unir PDF = Merge PDF
Unir todos PDF da pasta = Merge all PDF on folder

How does it work from the user perspective:
The user must set a folder with only PDF files;
The files must be in the order they will be numerated, sugested 1.first_file.pdf, 2.second_file.pdf, 2.1. first_attach_second_file.pdf, 3.third_file.pdf and so on;
The user chooses this folder by clicking on the button ESCOLHER PASTA ;
In this folder there will be created a subfolder called NUMERADOS;
In this subfolder all the files from the parent folder will have their copies numerated, the ORIGINAL FILES WILL NOT BE CHANGED;
The user will be able to merge the numerated files by clicking on UNIR PDF;
Merging files without numerating may require to create a NUMERADOS folder with the files and tho choose the parent folder;

How does it work from the developer perspective (useful if adaptations are needed):
The program requires path modules such as os, io, shutil, time, datetime;
The PyPDF2 library is used to parse and merge pages;
The fpdf is used to write new data on the existing pages (spent too much time trying to find one library that did both, without success);
Actualy fpdf creates a blank page with the desired text, further explanation follows below;
The natsorted library is used to sort the order from the files in folder;
Tkinter is used for the GUI.

Explanation of the code:
Tkinter is initiated with a StringVar for showing the path of the folder;
Every function is within the class App;
The screen, frames and layout are initiated;
The browse function ask the directory and set the global StringVar as path;
The about and licence function are pop-ups;
The frames are set;
The layout  menus are set and the buttons call the functions;
The new_content function deals with the added text to the PDF, it is called by the numerar function which is called throught its button;
here one can make its own adaptations,
currently top-right keeps the global page count 'Página 1' (Page 1),
botton-left of the page has the file partial count 'Página 2 de 10' (Page 2 of 10).
botton-right has the date and time;
Funcion numerar makes the hardwork, dealing with paths, creating a new folder, sorting files, parsing files, parsing pages, calling FPDF to create blank pages, 
overlaying these pages on the actual destination, compiling and opening a Ready ('Pronto') pop-up;
The merge function mimics the preparations of numerar function and the proceeds to merging using PyPDF2 merger.


