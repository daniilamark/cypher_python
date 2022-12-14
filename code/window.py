from tkinter import *
from tkinter import scrolledtext, ttk, filedialog

from main import *

def encryptText():
    # res = "Привет {}".format(txt.get())
    # res = vigenere_encrypt(getEntryTxt(), getEntryKey())
    res = vigenere_encrypt(getEntryTxt(), getEntryKey())
    print(getEntryTxt())
    result_txt.insert(INSERT, res)

def dencryptText():
    res = vigenere_decrypt(getEntryTxtDec(), getEntryKeyDec())
    print(getEntryTxtDec())
    result_txt_dec.insert(INSERT, res)


def all_clear():
    # result_txt.configure(state='normal')
    key_entry.delete(0, END)
    result_txt.delete('1.0', END)
    entry_txt.delete('1.0', END)

def all_clear_dec():
    # result_txt.configure(state='normal')
    key_entry_dec.delete(0, END)
    result_txt_dec.delete('1.0', END)
    entry_txt_dec.delete('1.0', END)


def downloadFileEnc():
    # entry_txt.delete('1.0', END)
    # result_txt.insert(INSERT, res)
    f_to_open = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_to_open = open(f_to_open, 'r', encoding='utf-8')
    txt_from_file = file_to_open.read()
    entry_txt.insert(INSERT, txt_from_file)

def downloadFileDec():
    # entry_txt.delete('1.0', END)
    # result_txt.insert(INSERT, res)
    f_to_open = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_to_open = open(f_to_open, 'r', encoding='utf-8')
    txt_from_file = file_to_open.read()
    entry_txt_dec.insert(INSERT, txt_from_file)


def savefile():
    try:
        path = filedialog.asksaveasfile(filetypes=(("Text files", "*.txt"), ("All files", "*.*"))).name
        # window.title('Notepad - ' + path)

    except:
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(result_txt.get('1.0', END))

    # text_zone.edit_modified(0)


window = Tk()
window.title("Маркин")
window.geometry('800x600')
window.iconbitmap('private_key.ico')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Шифровать')
tab_control.add(tab2, text='Дешифровать')

label_key = Label(tab1, text='Введите ключ')
label_key.grid(column=0, row=0)

key_entry = Entry(tab1, width=40)
key_entry.focus()
key_entry.grid(column=1, row=0)

label_txt = Label(tab1, text='Введите текст')
label_txt.grid(column=0, row=1)

entry_txt = scrolledtext.ScrolledText(tab1, width=28, height=10)
entry_txt.grid(column=1, row=1)

btn_download = Button(tab1, text="Загрузить", command=downloadFileEnc)
btn_download.grid(column=0, row=2)
btn_encrypt = Button(tab1, text="Шифровать!", command=encryptText)
btn_encrypt.grid(column=1, row=2)
btn_clear = Button(tab1, text="Очистить", command=all_clear)
btn_clear.grid(column=2, row=2)
btn_save = Button(tab1, text="Сохранить", command=savefile)
btn_save.grid(column=3, row=2)

result_txt = scrolledtext.ScrolledText(tab1, width=28, height=10)
result_txt.grid(column=2, row=1)


def getEntryKey():
    response = str(key_entry.get())
    return response


def getEntryTxt():
    response = entry_txt.get("1.0", END).replace('\n', '').replace('\r', '')
    return response


###############################
# TAB 2
###############################

label_key_dec = Label(tab2, text='Введите ключ')
label_key_dec.grid(column=0, row=0)

key_entry_dec = Entry(tab2, width=40)
key_entry_dec.focus()
key_entry_dec.grid(column=1, row=0)

label_txt_dec = Label(tab2, text='Введите текст')
label_txt_dec.grid(column=0, row=1)

entry_txt_dec = scrolledtext.ScrolledText(tab2, width=28, height=10)
entry_txt_dec.grid(column=1, row=1)

btn_download_dec = Button(tab2, text="Загрузить", command=downloadFileDec)
btn_download_dec.grid(column=0, row=2)
btn_encrypt_dec = Button(tab2, text="Дешифровать!", command=dencryptText)
btn_encrypt_dec.grid(column=1, row=2)
btn_clear_dec = Button(tab2, text="Очистить", command=all_clear_dec)
btn_clear_dec.grid(column=2, row=2)
btn_save_dec = Button(tab2, text="Сохранить", command=savefile)
btn_save_dec.grid(column=3, row=2)
result_txt_dec = scrolledtext.ScrolledText(tab2, width=28, height=10)
result_txt_dec.grid(column=2, row=1)

def getEntryKeyDec():
    response = str(key_entry_dec.get())
    return response

def getEntryTxtDec():
    response = entry_txt_dec.get("1.0", END).replace('\n', '').replace('\r', '')
    return response

tab_control.pack(expand=1, fill='both')
window.mainloop()