# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:12:08 2015

@author: Ezequiel
"""

from sys import stdin

def multiplicate(a,b):
    res = ''
    sign = ''
    letters = '1ijk'
    table = [['1','i','j','k'],['i','-1','-k','j'],['j','k','-1','-i'],['k','-j','i','-1']]
    if (a.find('-')!=-1 and b.find('-')==-1):
        sign = '-'
        a = a.replace('-','')
    elif (a.find('-')==-1 and b.find('-')!=-1):
        sign = '-'
        b = b.replace('-','')
    posA = letters.find(a)
    posB = letters.find(b)
    res = table[posB][posA]
    #print res,sign
    if res.find('-')!=-1 and sign=='-':
        res = res.replace('-','')
    else:
        res = sign+res
    return res

def resolve(s):
    res = ''
    i=0
    acum = s[i]
    while i<len(s)-1:
       acum = multiplicate(acum,s[i+1])
       i+=1
    res = acum
    return res

def main():
    T = int(stdin.readline())
    for i in range(T):
        # Vars
        res = 'NO'
        aux = stdin.readline().replace('\n','').split(' ')
        L = int(aux[0])
        X = int(aux[1])
        aux = stdin.readline().replace('\n','')
        inp = aux*X
        #print inp
        ind = 0
        l = 'i'
        acum = ''
        if (len(inp) >= 3):
            while (ind<len(inp)):
                #l!='k'
                substr = inp[ind]
                #acum = resolve(acum+substr)
                acum = multiplicate(acum,substr)
                if acum==l:
                    ind += 1
                    acum = ''
                    if l=='i':
                        l = 'j'
                    elif l=='j':
                        l = 'k'
                    if l=='k':
                        #res = 'YES'
                        break
                else:
                    ind += 1
            substr = inp[ind:]
            if len(substr)>0:
                if resolve(substr)=='k':
                    res = 'YES'

        print 'Case #'+str(i+1)+': '+res


if __name__=='__main__':
    main()
    #print resolve('-1i')
    #print multiplicate('-1','i')
