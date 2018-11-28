#! /usr/bin/python

#  (c) 2010 Wott (http://wott.net.ru/ , wott@gmail.com)

__author__="Wott"
__date__ ="$08.05.2010 3:30:26$"

import sys

def case(N,K):
    return('ON' if not (K+1)&((1<<N)-1) else 'OFF')

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: %s in.file out.file" % sys.argv[0])
        return
    with open(args[0]) as infile:
        with open(args[1],'w') as outfile:
            T = int(infile.readline())
            for i in range(T):
                N,K=[int(i) for i in infile.readline().rstrip().split()]
                c = case(N,K)
                outfile.write("Case #%s: %s\n" % (i+1,c))


def snap(n,k):
    if n==0: return 'ON'
    if k==0: return 'OFF'
    state=[False]*n
    #print("START: %s",state)
    for i in range(k):
        for j in range(n):
            state[j]=not state[j]
            if state[j]: break
        #print("%d: %s" % (i,state))
    for j in range(n):
        if not state[j]: return 'OFF'
    return 'ON'

def test():
    for N in range(10):
        for K in range(50):
            find = snap(N,K)
            #calc = 'ON' if K%2**N==(2**N-1) else 'OFF'
            calc = 'ON' if not (K+1)&((1<<N)-1) else 'OFF' # if K+1 trailing with N zero - & 2**N-1
            print("%d,%d -> %s == %s" % (N,K,snap(N,K),calc))


if __name__ == '__main__':
    main()
