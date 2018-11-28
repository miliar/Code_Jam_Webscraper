# -*- coding: utf-8 -*-
fname = "C-small-attempt0"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

def euclid(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
    
def itereuclid(seq):
    seq = iter(seq)
    gcd = next(seq)
    for n in gcd:
        gcd = euclid(gcd, n)
    return gcd
    
def findnote(othernotes, L, H):
    if L == 1:
        return 1
    
    for note in xrange(L, H+1):
        for othernote in othernotes:
            if (note % othernote) and (othernote % note):
                break
        else:
            return note
    
    return "NO"

numcases = gcj_read()[0]

for caseno in range(numcases):
    N, L, H = gcj_read()
    othernotes = gcj_read()
    
    note = findnote(othernotes, L, H)
    outstr = str(note)
    
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
