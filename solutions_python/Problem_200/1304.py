#!/usr/bin/python

t = int(raw_input())  # read a line with a single integer


def tidy(n):
    rewrite=0
    tab =[int(c) for c in str(n)]
    for i in range(len(tab)-1):
        if rewrite:
            tab[i]=9
        elif tab[i] > tab[i+1]:
            tab[i] = tab[i]-1
            rewrite = 1

    if rewrite:
        tab[i+1]=9
    num = int(''.join(map(str,tab)))
    return num

def uglytidy(n):
    m=tidy(n)
    if m==n:
        return m
    else :
        return uglytidy(m)

for i in xrange(1, t + 1):
  tt = [int(s) for s in raw_input()]  # read a list of integers, 2 in this case
  num2 = int(''.join(map(str,tt)))
  print "Case #{}: {}".format(i, uglytidy(num2))
