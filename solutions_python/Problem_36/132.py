#!/usr/bin/python

import sys
#"welcome to code jam"
#

#

#Input
 	
#elcomew elcome to code jam
#wweellccoommee to code qps jam
#welcome to codejam

def cal(a, b):
#    a = "welcome to code jam"
#    b = "elcomew elcome to code jam"

    # 1. construct the shelf

    shelf = []
    for i in range(0, len(a)):
        shelf.append([])

    for i in range(0,len(b)):
        c = a.find(b[i])
    #    print c, b[i]
        while c != -1:
            shelf[c].append([i,0])
            c = a.find(b[i], c+1)

    #print shelf

    # n[k] = len(shelf[k])
    n = []
    for i in range(0, len(a)):
        n.append(len(shelf[i]))
    #print n

    # 2. traverse from the last level

    i = len(a) - 1
    for j in range(0, len(shelf[i])):
        shelf[i][j][1] = 1

    for i in range(len(a)-2, -1, -1):
        cur = i
        low = i+1
        j1 = n[cur]-1
        j2 = n[low]-1
        sum = 0
    #    print cur, low, j1, j2
        
        while j2>=0 and j1>=0:
    #        print shelf[cur][j1][0], shelf[low][j2][0]
            if shelf[cur][j1][0] > shelf[low][j2][0]:
                shelf[cur][j1][1] = sum
                j1 -= 1
            else:
                sum += shelf[low][j2][1]
                j2 -= 1
        for j in range(j1, -1, -1):
            shelf[cur][j][1] = sum
            
    #    sys.exit(0)

    count = 0
    for i in range(0,n[0]):
        count += shelf[0][i][1]
    return count

a = "welcome to code jam"

infile = "C-large.in"
fin = open(infile)

outfile = "C-large.out"
fout = open(outfile, "w+")

num = fin.readline()

for i in range(0,int(num)):
    haha = cal(a, fin.readline()) % 10000
    fout.write( "Case #%d: %04d\n" % (i+1, haha))