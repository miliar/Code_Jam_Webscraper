from __future__ import division
import numpy as np

datafile = "A-small-attempt1.in"
outfile = "Asmout1.txt"

def fileread(filename):
    f = open(filename, "r")
    mainline = f.read()
    data = np.fromstring(mainline.replace("\n", " "), dtype = int, sep = ' ')
    return data

def filewrite(string, filename):
    f = open(filename, "a")
    f.write(string)
    f.close()

def hits(deck, row):
    return deck[4*row-4:4*row]


def matcher(hit1, hit2):
    card = 0
    totalhits = 0
    for i in hit1:
        tmp2 = hit2 - i
        matches = 4 - np.count_nonzero(tmp2)
        totalhits += matches
        if totalhits > 1:
            return -1  # Bad magician!

        if matches == 1:
            card = hit2[tmp2 == 0]
    if card == 0:
        return 0  # Cheater!
    else:
        return card

data = fileread(datafile)

cases = int(data[0])
betterdata = data[1:]

bestdata = betterdata.reshape((2*cases, 17))

for i in range(cases):
    hit1 = hits(bestdata[2*i,1:],bestdata[2*i,0])
    hit2 = hits(bestdata[2*i+1,1:],bestdata[2*i+1,0])
    magic = matcher(hit1, hit2)
    if magic < 0:
        filewrite("Case #"+str(i+1)+": Bad magician!\n", outfile)
    elif magic == 0:
        filewrite("Case #"+str(i+1)+": Volunteer cheated!\n", outfile)
    else:
        filewrite("Case #"+str(i+1)+": "+str(int(magic))+"\n", outfile)