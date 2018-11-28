#!/usr/bin/python

f=open('tidy_numbers_large.in', 'r')
output=open('tidy_numbers_large.out', 'w')

cases=int(f.readline())

def tidy(i):
    l=[int(c) for c in str(i)]
    return l == sorted(l)

for case in range(cases):
    x=int(f.readline().replace("\n",""))
    digits=len(str(x))
    l=[x]
    for i in range(digits):
        l.append(x - (x % (10 ** i)) - 1)
    value=max([i for i in l if tidy(i)])
    #print "Case #%i: %i" % (case+1,value)
    output.write ("Case #%i: %i\n" % (case+1, value))
