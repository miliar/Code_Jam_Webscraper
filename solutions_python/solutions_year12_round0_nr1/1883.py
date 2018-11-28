#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

T = [
     ("ejp mysljylc kd kxveddknmc re jsicpdrysi",
      "our language is impossible to understand"),
     ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
      "there are twenty six factorial possibilities"),
     ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
      "so it is okay if you want to just give up")
     ]


def analyze(T):
    M = {}
    for t in T:
        ciphertext,plaintext = t
        assert len(ciphertext) == len(plaintext)
        for c,p in zip(ciphertext,plaintext):
            if c == ' ':
                assert p == ' '
                continue
            if c not in M:
                M[c] = p
            else:
                assert M[c] == p
    return M 
    
    
M = analyze(T)

M['z'] = 'q'
M['q'] = 'z'

M[' '] = ' '

#print 'analyzed, len(M)==',len(M)
#print M
#
#assert M['e'] == 'o'
#assert M['y'] == 'a'
#assert M['q'] == 'z'
#
#alphabet = [chr(ic) for ic in range(ord('a'),ord('z')+1)]
#
#ML = M.keys()
#for c in alphabet:
#    if c not in ML:
#        print 'not found in cipher:',c
#
#MV = M.values()
#assert len(set(MV)) == len(MV)
#for c in alphabet:
#    if c not in MV:
#        print 'not found in plain:',c


def decipher(ciphertext):
    S = [M[c] for c in ciphertext]
    return ''.join(S)


T = int(ifs.readline())
for t in range(1,T+1):
    ciphertext = ifs.readline().strip()
    plaintext = decipher(ciphertext)
    ofs.write('Case #%d: %s\n' % (t,plaintext))
