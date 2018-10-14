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


infile = open('B-small-attempt0.in','r')
outfile = open('output.txt','w')


cases = eval(infile.readline())
ans = []

for i in range(cases):
    mat = []# the matrix
    dim = [] # matrix dimensions
    col =[] # columns to del
    rows = []# rows to del
    nm = infile.readline().split()
    #print(nm)
    dim.append(eval(nm[0]))
    dim.append(eval(nm[1]))
    #print(dim)
    #print(dim[1])
    for j in range(dim[0]):
        z = infile.readline().split()
        #for k in range(len(z)):
        #    z[k] = eval(z[k])
        mat.append(z)
    #print(mat)
    if dim[0] == 1 or dim[1] == 1:
        ans.append('y')
        continue

    test = False
    for l in range(dim[0]):
        #print(l)
        for m in range(dim[1]-1):
            #print(m)
            if mat[l][m] == '1' and mat[l][m+1] == '1':
                test = True
            else:
                test = False
                break
        if test == True:
            rows.append(l)

    test1 = False
    for ll in range(dim[1]):
        for mm in range(dim[0]-1):
            if mat[mm][ll] == '1' and mat[mm+1][ll] == '1':
                test1 = True
            else:
                test1 = False
                break
        if test1 == True:
            col.append(ll)


    #print(rows)
    #print(col)


    for ele in rows:
        for num in range(dim[1]):
            mat[ele][num] = 0
    for el in col:
        for nu in range(dim[0]):
            mat[nu][el] = 0

    #print(mat)
    #final check!
    ets = True
    for fi in range(dim[0]):
        for na in range(dim[1]):
            if mat[fi][na] == '1':
                ets = False
    if ets == True:
        ans.append('y')
    else:
        ans.append('n')




#print(ans)
for i in range(cases):
    if ans[i] == 'n':
        print('Case #',i+1,': NO',sep ='', file = outfile)
    else:
        print('Case #',i+1,': YES',sep ='', file = outfile)



infile.close()
outfile.close()










