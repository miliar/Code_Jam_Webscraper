#!/usr/bin/env python
import sys

#############
##Functions##
#############

def bf(A,B,K):
    count = 0
    for a in xrange(A):
        for b in xrange(B):
            if a&b < k: count += 1
    return count

##############
##File Input##
##############
path = 'input.in'
if len(sys.argv)>1: path = sys.argv[1]

try:
    f = open(path, 'r')
except:
    quit("Error opening file: %s" % path)

data = f.read().splitlines()
f.close()

#Trim extra data from end of file
while data[-1] == '':
    data = data[:-1]
while data[0] == '':
    data = data[1:]

trials = int(data[0])

########
##Main##
########
#for trial in [0]:
for trial in range(trials):
    x1 = map(int, data[trial*1 + 1].split(" "))

    print "Case #%d:" % (trial +1),
    [a, b, k] = x1

#    print "a", a, "b",b, "k",k
    print bf(a,b,k)
