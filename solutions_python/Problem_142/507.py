from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

def reducethis(string):
    theset = ''
    predc = 'Q'

    for c in string:
        if c != predc:
            theset += c

        predc = c

    return theset

def reducethisnumbers(string):
    theset = ''
    count = []

    i = 0

    while (i < len(string)):
        
        j = i

        while (j < len(string)) and string[i] == string[j]:
            j += 1

        theset += string[i]
        count.append(j - i)

        i = j

    return (theset, count)

def anstwo(stringa, stringb):

    # print "*->", stringa, stringb

    seta, na = reducethisnumbers(stringa)
    setb, nb = reducethisnumbers(stringb)

    # print "sets:", seta, setb
    # print "nb:", na, nb

    if seta != setb:
        return "Fegla Won"
    else:

        sum = 0

        for i in range(0, len(na)):
            sum += abs(na[i] - nb[i])

        return sum

    return

T = int(stdin.readline())

for i in range(1,T+1):
    
    N = int(stdin.readline())

    string = {}

    for j in range(0,N):
        string[j], = stdin.readline().split()

    print "Case #" + str(i) + ":", 

    #print T, string
    print anstwo(string[0], string[1])
