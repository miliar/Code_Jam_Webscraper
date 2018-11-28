#!/usr/bin/python

def main():
    for case in range(input()):
        p, k, l=map(int, raw_input().split())
        fq=map(int, raw_input().split())
        fq.sort()
        fq.reverse()
        ret=0
        np=1
        i=0
        while i<l:
            j=0
            while j<k and i+j<l:
                ret+=fq[i+j]*np
                j+=1
            np+=1
            i+=k
        print "Case #%d: %d" % (case+1, ret)        
main()
