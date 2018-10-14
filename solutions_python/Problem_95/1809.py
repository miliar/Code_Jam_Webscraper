'''
Created on Apr 14, 2012

@author: Josh
'''

import string

if __name__ == '__main__':

    input_file = open ('one.txt', 'r')
    output_file = open('one_out.txt', 'w')
    
    cases = int(input_file.readline())
    
    for idx, line in enumerate(input_file, 1):
        out = line.translate(string.maketrans('abcdefghijklmnopqrstuvwxyz', 
                                              'YHESOCVXDUIGLBKRZTNWJPFMAQ'))
    
        print out
        s = 'Case #%i: %s' % (idx,out.lower())
        print s
        output_file.writelines([s])
    
#ejp mysljylc kd kxveddknmc re jsicpdrysi
#our language is impossible to understand
#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#there are twenty six factorial possibilities
#de kr kd eoya kw aej tysr re ujdr lkgc jv
#so it is okay if you want to just give up


