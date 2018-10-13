#!/usr/bin/env python
#encoding=utf-8

'''
author:		Eric Zhang(snow31450588@gmail.com)
date:		2012-04-14
purpose:	Google Code Jam Qualification Round
history:
	2012-04-14	Initial version
'''

import sys
import string

def maketrans():
    googlerese = """
    y qee
    ejp mysljylc kd kxveddknmc re jsicpdrysi
    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
    de kr kd eoya kw aej tysr re ujdr lkgc jv
    z
    """
    english = """
    a zoo
    our language is impossible to understand
    there are twenty six factorial possibilities
    so it is okay if you want to just give up
    q
    """
    #print googlerese, english
    #print string.lowercase
    dest = ''.join(googlerese.split())
    src = ''.join(english.split())
    #print dest, src
    trans = string.maketrans(dest, src)
    #for g in googlerese.splitlines():
    #    print string.translate(g, trans)
    return trans
    

def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %s\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        l = f.readline().strip()
        inputs.append(l)
    return inputs

def main(fin, fout):
    trans = maketrans()
    inputs = rf(fin)
    
    results = []
    for g in inputs:
        e = string.translate(g, trans)
        results.append(e)
    wf(fout,results)


if __name__=='__main__':
    fin = sys.argv[1]
    fout = sys.argv[1][:-2]+'out'
    main(fin, fout)
    