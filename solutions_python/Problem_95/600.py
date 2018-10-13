'''
Created on Apr 14, 2012

@author: namnx
'''
import sys

CIPHERS = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 
           'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
           'de kr kd eoya kw aej tysr re ujdr lkgc jv'] 

PLAINS = ['our language is impossible to understand',
          'there are twenty six factorial possibilities',
          'so it is okay if you want to just give up']

def read_input():
    pass


if __name__ == '__main__':
    cmap = {}
    for i in range(len(CIPHERS)):
        cipher = CIPHERS[i]
        plain = PLAINS[i]
        for j in xrange(len(cipher)):
            if cipher[j] == ' ': continue
            cmap[cipher[j]] = plain[j]
    cmap['q'] = 'z'
    cmap['z'] = 'q'
    
    f = open(sys.argv[1])
    t = f.readline().strip()
    t = int(t)
    for i in xrange(t):
        cipher = f.readline().strip()
        plain = ''
        for c in cipher:
            if c == ' ': plain += ' '
            else: plain += cmap[c]
        print 'Case #' + str(i+1) + ': ' + plain
    f.close()
    