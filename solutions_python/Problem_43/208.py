'''
Created on 13.09.2009

@author: Vlad Dumitrescu
'''

from math import pow

def alfanum_gen():
    R = []
    x = 0
    while x <= 9:
        R += "%i" % x
        x += 1
    x = ord('a')
    while x < ord('z') + 1:
        R += "%c" % x
        x += 1
    return R

def baseconvert(b, n):
    c = alfanum_gen()
    r = 0
    p = len(n) - 1
    for i in n:
        r += c.index(i) * pow(b, p)
        p -= 1
    return r

if __name__ == '__main__':
    # open input and output files
    fin = open('A-small.in', 'r')
    fout = open('A-small.out', 'w')
    
    T = int(fin.readline())
    j = 0
    while T > 0:
        j += 1
        fout.write('Case #' + str(j) + ': ')
        
        S = fin.readline().strip()
        
        chars = alfanum_gen()
        aux = chars[0]
        chars[0] = chars[1]
        chars[1] = aux
        d = {}
        next = 0
        r = ''
        for c in S:
            if c not in d.keys():
                d[c] = chars[next]
                next += 1
            r += d[c]
        if next == 1: next = 2
        fout.write("%i\n" % baseconvert(next, r))
        T -= 1
    
    fin.close()
    fout.close()