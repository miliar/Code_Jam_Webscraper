#!/usr/bin/env python
#-*- coding:utf-8 -*-

ABC = "abcdefghijklmnopqrstuvwxyz"

def gdict(): # Initialize d
    cipher = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    plain =  "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

    d = {'y': 'a', 'q': 'z', 'e': 'o'}
    
    for i in xrange(len(cipher)):
        d[cipher[i]] = plain[i]
        
    for c in ABC:
        if c not in d.values():
            d['z'] = c
        
    return d

def f(d, x):
    return d[x] # for map


def main():
    d = gdict()

    n = raw_input()
    T = int(n)
    
    for i in xrange(1, T+1):
        line = raw_input()
        ret = []
        for j in xrange(len(line)):
            ret.append(d[line[j]])
        print "Case #"+str(i)+":", str(ret).strip("[]").replace("', '", "").strip("''")

    
if __name__ == '__main__':
    main()

