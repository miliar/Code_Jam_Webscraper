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

infile = open('A-small-attempt0.in','r')
outfile = open('out.txt','w')

cases = eval(infile.readline())
#print(first)
ans=[]

for r in range(cases):
    a=[]
    b=[]
    for j in range(4):
        c=[]
        d=[]
        for i in infile.readline():
            if i != '\n':
                c.append(i)
                d.append(i)
        a.append(c)
        b.append(d)
        del c
        del d
    infile.readline()




    for row in range(4):
        for col in range(4):
            if a[row][col] == 'T':
                #print('yay!')
                a[row][col] = 'X'
                b[row][col] = 'O'
                break
    print(a)
    print(b)


    #test to see if there is a win (o ,o wins)(x , x wins)(d , draw)(u , uncomplete)
    rc =False
    cc = False
    for n in range(4):
        if a[0][n] == a[1][n] == a[2][n] == a[3][n] == 'X' or b[0][n] == b[1][n] == b[2][n] == b[3][n] == 'X':
            ans.append('x')
            break
        elif a[0][n] == a[1][n] == a[2][n] == a[3][n] == 'O' or b[0][n] == b[1][n] == b[2][n] == b[3][n] == 'O' :
            ans.append('o')
            break
        elif a[n][0] == a[n][1] == a[n][2] == a[n][3] == 'X' or b[n][0] == b[n][1] == b[n][2] == b[n][3] == 'X':
            ans.append('x')
            break
        elif a[n][0] == a[n][1] == a[n][2] == a[n][3] == 'O' or b[n][0] == b[n][1] == b[n][2] == b[n][3] == 'O':
            ans.append('o')
            break
        elif a[0][0] == a[1][1] == a[2][2] == a[3][3] == 'O' or b[0][0] == b[1][1] == b[2][2] == b[3][3] == 'O':
            ans.append('o')
            break
        elif a[0][0] == a[1][1] == a[2][2] == a[3][3] == 'X' or b[0][0] == b[1][1] == b[2][2] == b[3][3] == 'X':
            ans.append('x')
            break
        elif a[0][3] == a[1][2] == a[2][1] == a[3][0] == 'O' or b[0][3] == b[1][2] == b[2][1] == b[3][0] == 'O':
            ans.append('o')
            break
        elif a[0][3] == a[1][2] == a[2][1] == a[3][0] == 'X' or b[0][3] == b[1][2] == b[2][1] == b[3][0] == 'X':
            ans.append('x')
            break
        else:
##            temp = False
##            for g in range(4):
##                for gg in range(4):
##                    if a[g][gg] == '.':
##                        ans.append('u')
##                        temp = True
##                        break
##                if temp == True:
##                    break
##            else:
##                ans.append('d')
            temp = 0
            for g in range(4):
                for gg in range(4):
                    if a[g][gg] == '.':
                        temp += 1
            if temp == 0:
                ans.append('d')
                break
            else:
                ans.append('u')
                break
# output
for d in range(len(ans)):
    if ans[d] == 'x':
        print('Case #',d+1,': X won',sep = '',file = outfile)
    elif ans[d] == 'o':
        print('Case #',d+1,': O won',sep = '',file = outfile)
    elif ans[d] == 'u':
        print('Case #',d+1,': Game has not completed',sep = '',file = outfile)
    elif ans[d] == 'd':
        print('Case #',d+1,': Draw',sep = '',file = outfile)




infile.close()
outfile.close()




























