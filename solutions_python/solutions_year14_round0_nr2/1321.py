from __future__ import division

import os, sys
# os.chdir('/home/JJ/Downloads')
inputfile = open(r'/home/jj/Downloads/{}'.format(sys.argv[1]), 'r')
# os.chdir('/home/JJ/Desktop')
outputfile = open(r'/home/jj/Desktop/out.txt', 'w')

def worth_buying(C, F, X, earn_rate):

    if (C / earn_rate + X / (earn_rate + F)) < (X / earn_rate):
        return True
    else:
        return False

def calc(C, F, X, earn_rate=2):

    acc = 0
    while worth_buying(C, F, X, earn_rate):
        acc +=  C / earn_rate
        earn_rate += F
    else:
        acc += X / earn_rate

    return acc

t = inputfile.readlines()
T = int(t.pop(0))
for index, line in enumerate(t):
    case = index + 1
    C, F, X = map(float, line.split(" "))
    ret = calc(C, F, X)
    outputfile.write("Case #{}: {}\n".format(case, ret))

