#!/usr/bin/env python 
import copy
import sys
import os 
debug = 0
def solve(smax, sary):
    print smax , sary 
    add = 0 
    stand = 0 
    for i in range(0,smax+1):
        delta = i - stand 
        print delta
        if delta > 0 :         
           add += delta 
           stand += delta
        stand +=  sary[i] 
        print add, stand
    return add
def foo(filename):
    f = open(filename,"r")
    output = open("%s.out"%filename, 'w')
    context = f.read().split('\n')    
    C = int(context[0])  # C, the number of test cases
    
    k = 1
    for i in range(0,C):
        data = context[i+1]
        a = data.split()
 #       print a; 
        n = int(a[0])
        sary = [int(x) for x in a[1]]
#        print n , sary; 
        output.write( "Case #%d: %s\n"%(i+1, solve(n, sary)))
    f.close()
    output.close()
  
def main():
    if len(sys.argv) > 1:
        inputfile = sys.argv[1] 
    else:
        inputfile = "input"
    foo(inputfile)
            
if __name__ == "__main__":
    main()

