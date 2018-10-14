#!/usr/bin/python
from math import sqrt
import time

caso_completo = []
trovato = 0
win = ''
cntcasi = 1


def is_square(integer):
    root = sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

def palindrome(n):
    d = []
    while (n > 0):
        d.append(n % 10)
        n //= 10
    for i in range(len(d)/2):
        if (d[i] != d[-(i+1)]):
            return "Fail."
    return "Pass."

with open('small.in') as f:
    i = 0
    for x in f.readlines(2):
        if i != 0:

            x = x.replace('\n','')
            #print x
            low = x.find(' ')
            min = int(x[:low])
            max = int(x[low+1:])
            #print min
            #print max
            c = min
            count = 0
            while (c <= max):
                if is_square(c) == True:
                    rad = sqrt(c)
                    #print rad
                    if palindrome(rad) == 'Pass.' and palindrome(c) == 'Pass.':
                        #print "%d %d " % (c, quad)
                        count +=1
                c +=1

            print "Case #%d: %d" % (i,count)


        i += 1
