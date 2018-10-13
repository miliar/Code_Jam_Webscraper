'''
Created on Feb 22, 2017

@author: cturkarslan
'''
###REDIRECT IO
import sys
import re

#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output_1.txt', 'w')


#sys.stdin = open('A-small-attempt0.in' ,'r')
sys.stdin = open('A-large.in' ,'r')
sys.stdout = open('output_2.txt' , 'w')

def checkEqual3(lst):
   return lst[1:] == lst[:-1]


T = int(input())
for t in range(T):
    R,C = map(int,input().split())
    cake = []
    for r in range(R):
         row = list(input())
         cake.append(row)

#    print(cake)

    duplicates = set()


    for r in range(1,R):
        if (cake[r].count("?") == len (cake[r])):
            cake[r] = cake [r-1]
            duplicates.add((r,r-1))
    for r in reversed(range(R-1)):
            if (cake[r].count("?") == len(cake[r])):
                cake[r] = cake[r + 1]
                duplicates.add((r, r + 1))

    for r in range(R):
        last_el = -1
        for c in range(C):
            if(cake[r][c] is not "?"):
                last_el = cake[r][c]
            else :
                if(last_el != -1 ):
                    cake[r][c] = last_el

    for r in range(R):
        last_el = -1
        for c in reversed(range(C)):
            if(cake[r][c] is not "?"):
                last_el = cake[r][c]

            else :
                if(last_el != -1 ):
                    cake[r][c] = last_el


    for dup in duplicates:
        cake[dup[0]] = cake[dup[1]]


    print("Case #%d:" % (t + 1))
    for r in range(R):
            print ("".join(cake[r]))



if __name__ == '__main__':
    pass