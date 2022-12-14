# -*- coding: utf-8 -*-
def vigenere(
    text: str,
    key: str,
    alphabet="'"+' .,!";:?()-—0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    encrypt=True
):

    result = ''

    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])

        if encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]

    return result


def vigenere_encrypt(text, key):
    return vigenere(text=text, key=key, encrypt=True)


def vigenere_decrypt(text, key):
    return vigenere(text=text, key=key, encrypt=False)


#file = open('input.txt', 'r', encoding='utf-8')
#with open('input.txt', 'r', encoding='utf-8') as file:
#    response=file.read().replace('\n', '').replace('\r', '')

#file2 = open('output.txt', 'w', encoding='utf-8')
#word = file.read()
#file.close()

#a = vigenere_encrypt(response, 'secretWORD')
#print(a)
#file2.write(a)
#file2.close()
#b = vigenere_decrypt(a, 'secretWORD')
#print(b)