#!/usr/bin/env python

import sys

def invites(Smax,S):
    total = int(S[0])
    inv = 0
    for i in range(1,Smax+1):
        if total<i:
            ninv = i-total
            inv += ninv
            total += ninv
        total += int(S[i])
    return inv

def main():
    nb_cases = int(sys.stdin.readline())
    for c in range(1,nb_cases+1):
        donnees = sys.stdin.readline().split()
        print 'Case #%d: %d' % (c,invites(int(donnees[0]),donnees[1]))

main()
