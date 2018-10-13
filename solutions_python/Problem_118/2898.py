'''
Created on Apr 13, 2013

@author: Osborn
'''
import math

def mysolution(input):
    
    def palindrome(x):
        x = str(x)
        if x==x[::-1]:
            return int(x)
        
    list=[]
    square_pal=[]
    square_num = [x*x for x in range(1000)]
    for x in xrange(1000):
        if palindrome(x):
            square_pal.append(x*x)
    for x in xrange(int(input[0]), int(input[1])+1):
        if x in square_pal and palindrome(x):
            list.append(x)
    return str(len(list))

g=open('output1', 'w')
with open('C-small-attempt0.in') as f:
    testcase = f.readline()
    list=[]
    for x in xrange(int(testcase)):
        list.append(f.readline().split())
    print list
    for y, x in enumerate(list):
        g.write('Case #%d: ' %(y+1))
        g.write(mysolution(x))
        g.write('\n')


