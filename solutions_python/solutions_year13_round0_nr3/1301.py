#!/usr/bin/env python

import math

def read_input(f):
    line = f.readline()
    words = line.split()
    
    A = int(words[0])
    B = int(words[1])    

    return A,B

def is_fair(n):
    s = str(n)
    return s==s[::-1]

def is_square(n):
    r = math.sqrt(n)
    return r == math.trunc(r)
        
def is_fair_and_square(n):
    if is_fair(n):
        if is_square(n):
            r = math.sqrt(n)
            r = math.trunc(r)
            if is_fair(r):
                return True
    return False        

def find_first_square(A,B):
    for n in range(A,B+1):
        if is_square(n):
            return n
    return None    

def search_by_square(B,n):
    r = int(math.sqrt(n))
    count = 0
    
    while n <= B:

        if is_fair_and_square(n):
            #print 'n', n
            count = count + 1
            
        r += 1
        n = r*r
    
    return count
    
def main():  
    #f = open('C-input.txt', 'r')
    f = open('C-small-attempt1.in', 'r')
    #f = open('C-large.in', 'r')
    T = int(f.readline())

    out = open('output.txt', 'w')
    for i in range(T):   
        
        A,B = read_input(f)
        
        #print 'Case',i, '--', 'A =',A,'B =',B
        
        n = find_first_square(A,B)
        
        out.write('Case #'+str(i+1))
        if n != None:
            out.write(': '+str(search_by_square(B,n)))   
        else:
            out.write(': 0')
        out.write('\n')
        
        #raw_input()
                  
if __name__ == '__main__': 
    main()
