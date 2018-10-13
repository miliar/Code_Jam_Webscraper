# -*- coding: utf-8 -*-

# QUALIFICATION ROUND 2012 - PROBLEM A
# Author: Paul Mollet-Padier

def QR2012_A():
    def googlerese(s):
        code = ['y',
                'h',
                'e',
                's',
                'o',
                'c',
                'v',
                'x',
                'd',
                'u',
                'i',
                'g',
                'l',
                'b',
                'k',
                'r',
                'z',
                't',
                'n',
                'w',
                'j',
                'p',
                'f',
                'm',
                'a',
                'q']
        g = ''
        for word in s.split(' '):
            for letter in word:
                if ord(letter)-97 >= 0:
                    g += code[ord(letter)-97]
            g += ' '
        return g
    
    f = open('A-small-attempt1.in')
    o = open('A-small-attempt1.out', 'w')
    n = int(f.readline())

    for i in range(n):
        o.write("Case #" + str(i+1) + ': '+ googlerese(f.readline())+ '\n')
