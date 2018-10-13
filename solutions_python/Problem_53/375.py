#!/usr/bin/env python

INFILENAME = 'A-large.in'
#INFILENAME = 'input.in'
OUTFILENAME = 'output.out'

def initIO():
    read = open(INFILENAME, 'rt')
    write = open(OUTFILENAME, 'wt')
    return (read, write)

def deinitIO(read, write):
    read.close()
    write.close()

def main():
    r, w = initIO()
    
    T = int(r.readline())
    current = 1
    
    while (T>0):
        [N,K] = [int(x) for x in r.readline().split()]
        #is_on = (1 << (N-1)) & K != 0
        is_on = ((1 << N) & K) != ((1 << N) & (K+1))
        is_on_text = "ON" if is_on else "OFF"
        w.write( "Case #{0}: {1}\n".format(current, is_on_text) )
        
        T -= 1
        current += 1
        
    
    deinitIO(r, w)

main()