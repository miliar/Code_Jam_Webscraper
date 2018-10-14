#! /usr/bin/python2.7

import os

def lolcount(stri):
    i = len(stri) - 1
    count = 0
    while i >= 0  and stri[i] == '0':
        i = i - 1
    while i >= 0:
        if stri[i] == '0':
            count = count + 1
        i = i - 1
    return count


f = open('inputfile', 'r')
outf = open('outputfile', 'w')
mystr = f.read()
mytab = mystr.split('\n')
testnumber = int(mytab[0])

values = []
shylevel = 0
friends = 0
iteri = 0
loliter = 0
for i in mytab[1:-1]:
    values.append(i.split(' ')[1])
    iteri = iteri + 1
for i in values:
    iteri = 0
    for y in i:
        if iteri < shylevel:
            shylevel = shylevel + int(y)
        else:
            friends = friends + 1
            shylevel = shylevel + int(y) + 1
        iteri = iteri + 1
    loliter = loliter + 1
    outf.write("Case #" + str(loliter) + ": " + str(friends - 1) + '\n')
    shylevel = 0
    friends = 0

