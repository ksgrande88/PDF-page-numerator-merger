import os
import io
import time
import shutil
import tkinter
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader, PdfMerger
from fpdf import FPDF
from datetime import datetime
from natsort import os_sorted
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
folder_path = StringVar()


class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.layout()
        root.mainloop()

    def tela(self):
        self.root.title('Cmdo 5ª Bda C Bld - Utilidades PDF')
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.configure(background='#F0F0F0')

    def browse(self):
        global folder_path
        filename = filedialog.askdirectory()
        folder_path.set(filename)

    def sobre(self):
         messagebox.showinfo(title='Sobre',
                        message='Criado por Adriano Kleinert CASAGRANDE - Capitão\n'
                             'com recursos do Comando da 5ª Brigada de Cavalaria Blindada')

    def licenca(self):
         messagebox.showinfo(title='Licença',
                        message='CMIT License \n Copyright (c) [2023] [ADRIANO KLEINERT CASAGRANDE]\n'
'Permission is hereby granted, free of charge, to any person\n'
'obtaining a copy of this software and associated\n'
'documentation files (the "Software"), to deal in the Software\n'
'without restriction, including without limitation the rights\n'
'to use, copy, modify, merge, publish, distribute, sublicense,\n'
'and/or sell copies of the Software, and to permit persons to\n'
'the Software is furnished to do so, subject to the following\n'
'conditions:\n\n'
'The above copyright notice and this permission notice shall\n'
'be included in all copies or substantial portions of the\n'
'Software.\n\n'                             
'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY\n'
'OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT\n'
'LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
'FITNESS FOR A PARTICULAR PURPOSE AND NON\n'
'INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR \n'
'COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES\n'
'OR OTHER LIABILITY, WHETHER IN AN ACTION OF\n'
'CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF\n'
'OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR\n'
'OTHER DEALINGS IN THE SOFTWARE.')

    def frames(self):
        self.caput = Frame(self.root, bd=4, bg='#666666')
        self.caput.place(x=25, y=25, width=450, height=200)
        self.caput2 = Frame(self.root, bd=4, bg='#F0F0F0')
        self.caput2.place(x=40, y=40, width=420, height=170)
        self.num = Frame(self.root, bd=4, bg='#666666')
        self.num.place(x=25, y=250, width=210, height=200)
        self.num2 = Frame(self.root, bd=4, bg='#F0F0F0')
        self.num2.place(x=40, y=265, width=175, height=170)
        self.merg = Frame(self.root, bd=4, bg='#666666')
        self.merg.place(x=270, y=250, width=205, height=200)
        self.merg2 = Frame(self.root, bd=4, bg='#F0F0F0')
        self.merg2.place(x=285, y=265, width=175, height=170)

    def layout(self):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.browse)
        filemenu.add_separator()
        filemenu.add_command(label="Fechar", command=root.quit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)

        sobremenu = Menu(menubar, tearoff=0)
        sobremenu.add_command(label="Sobre...", command=self.sobre)
        sobremenu.add_separator()
        sobremenu.add_command(label="Licença...", command=self.licenca)
        menubar.add_cascade(label="Sobre", menu=sobremenu)
        root.config(menu=menubar)

        tit_pasta = Label(root, text='ESCOLHA DA PASTA', font=('arial', 16, 'bold'))
        tit_pasta.place(x=150, y=50)
        escolher = Button(root, text='Escolher pasta', command=self.browse, bd=4, font=('arial', 12))
        escolher.place(x=175, y=100, width=150, height=50)
        entry_pasta = Entry(root, width=60, textvariable=folder_path, bd=2)
        entry_pasta.place(x=70, y=170)

        tit_numerar = Label(root, text='NUMERAR', font=('arial', 14, 'bold'))
        tit_numerar.place(x=70, y=280)
        subtit_numer = Label(root, text='Qual o número da 1ª pág?', font=('arial', 10))
        subtit_numer.place(x=52, y=315)
        num_entry = Entry(root, width=5)
        num_entry.place(x=110, y=350)
        numerar = Button(root, text='Numerar', command=lambda: self.numerar(num_entry.get()),
                         bd=4, font=('arial', 12))
        numerar.place(x=70, y=380, width=120, height=50)

        tit_unir = Label(root, text='UNIR PDF', font=('arial', 14, 'bold'))
        tit_unir.place(x=320, y=280)
        subtit_unir = Label(root, text='Unir todos PDF da pasta', font=('arial', 10,))
        subtit_unir.place(x=302, y=330)
        unir = Button(root, text='Unir',  command=self.merge,
                      bd=4, font=('arial', 12))
        unir.place(x=320, y=380, width=120, height=50)

    def new_content(self, counter, file_counter, file_pages):
        fpdf = FPDF()
        fpdf.add_page()
        fpdf.set_font('Arial', size=12)
        fpdf.text(180, 10, f'Página {counter}')
        time_stamp = time.time()
        date_time = datetime.fromtimestamp(time_stamp)
        str_date_time = date_time.strftime("%d-%m-%Y %H:%M:%S")
        fpdf.text(160, 290, f'{str_date_time}')
        fpdf.text(10, 290, f'Pág {file_counter} de {file_pages}')
        return fpdf.output()

    def numerar(self, first_page_num):
        os.chdir(folder_path.get())
        p = Path(Path.cwd())
        if os.path.exists(p / 'NUMERADO'):
            shutil.rmtree(p / 'NUMERADO')
        os.makedirs(p / 'NUMERADO')
        files = []
        counter = int(first_page_num)
        for file in os.listdir(p):
            test_file = p / file
            if not test_file.is_dir():
                files.append(str(file))
        files = os_sorted(files)
        for pdf in files:
            reader = PdfReader(pdf)
            writer = PdfWriter()
            file_counter = 1
            for page in reader.pages:
                file_pages = len(reader.pages)
                page_overlay = PdfReader(io.BytesIO(self.new_content
                                         (counter, file_counter, file_pages))).pages[0]
                page.merge_page(page_overlay)
                writer.add_page(page)
                counter += 1
                file_counter += 1
            with open(p/'NUMERADO'/f'{pdf}', 'wb') as fp:
                writer.write(fp)
        counter = int(first_page_num)
        file_counter = 1
        messagebox.showinfo(title='Pronto',
                            message='Subpasta NUMERADO criada com arquivos numerados.')

    def merge(self):
        os.chdir(folder_path.get())
        p = Path(Path.cwd())
        if os.path.exists(p / 'NUMERADO'):
            os.chdir(p / 'NUMERADO')
            p = Path(Path.cwd())
        files = []
        merger = PdfMerger()
        for file in os.listdir(p):
            test_file = p / file
            if not test_file.is_dir():
                files.append(str(file))
        files = os_sorted(files)

        if 'PDFs UNIDOS.pdf' in files:
            os.unlink(p / 'NUMERADO' / 'PDFs UNIDOS.pdf')
        for pdf in range(len(files)):
            merger.append(files[pdf])
        merger.write('PDFs UNIDOS.pdf')
        merger.close()
        messagebox.showinfo(title='Pronto',
                            message='Arquivo "PDFs UNIDOS.pdf" criado.')

if __name__ == '__main__':
    App()
