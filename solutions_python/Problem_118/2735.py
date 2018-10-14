#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kirodh
#
# Created:     13/04/2013
# Copyright:   (c) kirodh 2013
# Licence:     dck
#-------------------------------------------------------------------------------
import math


def main():
    pass

if __name__ == '__main__':
    main()



infile = open('C-small-attempt0.in','r')
outfile = open('output.txt','w')

cases = eval(infile.readline())

ans = []


##def pali(v):
##    x1 = str(v)




for i in range(cases):
    squares = [] # for the numbers that are squares in the range
    inipali =[]
    a =[] # range list
    c = infile.readline()
    b = c.split(' ')
    for ele in b:
        a.append(eval(ele))
    #del b
    #print(b)
    #print(a)

    for i in range(a[0],a[1]+1):
        A = str(i)
        B=''
        for ii in A:
            B = ii +B
        if A == B:
            inipali.append(eval(A))

    for j in inipali:
        t = int(math.sqrt(j))
        if t**2 == j:
            squares.append(t)
    #print(squares)
    count = 0
    for k in squares:
        Aa = str(k)
        Ba=''

        for ia in Aa:
            Ba = ia +Ba
        if Aa == Ba:
            count += 1
    ans.append(count)
    count = 0

for y in range(len(ans)):
    print('Case #',y+1,': ',ans[y],sep='',file = outfile)







infile.close()
outfile.close()