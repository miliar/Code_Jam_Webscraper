#!/usr/bin/python

t = int(raw_input())  # read a line with a single integer

def flip(tt,i,k):
    for j in range(0,k):
        if tt[i+j]=="+":
            tt[i+j]="-"
        else :
            tt[i+j]="+"

#    print(tt)

def optiflip(tt,k):
    nb=0
    l=len(tt)-k
    for i in range(0,l+1):
        if tt[i]=="-":
            nb=nb+1
            flip(tt,i,k)

    for i in range(l,len(tt)):
        if tt[i]=="-":
            return "IMPOSSIBLE"

    return nb


for i in xrange(1, t + 1):
  tt,b =[(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, optiflip(list(tt), int(b)))
