'''
Created on 14 avr. 2012

@author: truc
'''

from string import maketrans
from string import ascii_lowercase

INPUT = '\n'.join(["3",
                   "ejp mysljylc kd kxveddknmc re jsicpdrysi",
                   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                   "de kr kd eoya kw aej tysr re ujdr lkgc jv"])

OUTPUT = '\n'.join(["our language is impossible to understand",
                    "there are twenty six factorial possibilities",
                    "so it is okay if you want to just give up])"])


def update_cipherbet(current_cipher_list, i, o):
    input_text = i.replace(' ', '')
    output_text = o.replace(' ', '')
    alphabet = ascii_lowercase
    cipherbet_list = current_cipher_list
    for i in range(len(input_text)):
        cipherbet_list[alphabet.index(input_text[i])] = output_text[i]
    return cipherbet_list


def problemA():
    in_filename = 'C:/tmp/A-small-attempt1.in'
    aInput = INPUT.splitlines()
    aOutput = OUTPUT.splitlines()
    T = int(aInput.pop(0))
    
    alphabet = ascii_lowercase
    cipherbet_list = [''] * len(alphabet)
    for i in range(T):
        text = aInput[i]
        expected = aOutput[i]
        cipherbet_list = update_cipherbet(cipherbet_list, text, expected)
        
        for i in range(len(alphabet)):
            if (cipherbet_list[i] == ''):
                cipherbet_list[i] = alphabet[i]
    
    cipherbet_list[alphabet.index('z')] = 'q'
    cipherbet_list[alphabet.index('q')] = 'z'
    cipherbet = ''.join(cipherbet_list)
    
    with open(in_filename) as fin:
        aInput = fin.readlines()
        T = int(aInput.pop(0))
        for i in range(T):
            text = aInput[i].replace('\n', '')
            trantab = maketrans(alphabet, cipherbet)
            text = text.translate(trantab)
            print 'Case %i: %s' % (i+1, text)


if __name__ == '__main__':
    problemA()
