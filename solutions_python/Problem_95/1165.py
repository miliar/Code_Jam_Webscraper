'''
Created on 14 avr. 2012

@author: gnugnu
'''
import GCJ

debug = True

dico = {' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q'}

def trans_chr(a):
    return dico[a]

class Run(object):
    def __init__(self, filename_input, filename_output):
        self.file_in = GCJ.InputFile(filename_input)
        self.file_out = GCJ.OutputFile(filename_output)
        
        for line in self.file_in:
            self.file_out.prt("".join(map(trans_chr, line)))

        self.file_out.close()
        
if __name__ == '__main__':
    start = Run("mini.in", "mini.out")
    start = Run("A-small-attempt0.in", "A-small-attempt0.out")