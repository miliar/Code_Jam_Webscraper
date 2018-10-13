#!/usr/bin/env python

from codejam import CodeJam

dict_ = {'q': 'z', 'z': 'q'}

sample_encrypted = ('ejp mysljylc kd kxveddknmc re jsicpdrysi '
                    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd '
                    'de kr kd eoya kw aej tysr re ujdr lkgc jv') 

sample_decrypted = ('our language is impossible to understand '
                    'there are twenty six factorial possibilities '
                    'so it is okay if you want to just give up')

def load_dict():
    for i, enc_letter in enumerate(sample_encrypted):
        dict_[enc_letter] = sample_decrypted[i]

def translate(text):
    translated = []
    for enc_letter in text:
        translated.append(dict_.get(enc_letter))
    
    return ''.join(translated)

def test_dict():
    assert translate(sample_encrypted) == sample_decrypted 


if __name__ == '__main__':
    load_dict()
    #test_dict()
    codejam = CodeJam('A-small-attempt0.in')
    codejam(translate)
