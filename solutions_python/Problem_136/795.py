#!/usr/bin/env python 
# import copy
# import os 
import sys
# debug = 0
    
def solve(data):
    data = data.split()
    C = float(data[0])
    F = float(data[1])
    X = float(data[2]) 
    # print C, F, X
    F0 = 2.0
    Fx = F0 
    t = 0.0
    while 1:
        dtStop = X/Fx  
        Fxx = Fx+F
        dtBuyNext =  C/Fx
        dtNext = dtBuyNext + X/Fxx 
        if dtStop < dtNext : 
            t = t + dtStop 
            break;
        t = t + dtBuyNext 
        Fx = Fxx 
    return t
def foo(filename):
    f = open(filename,"r")
    output = open("%s.out"%filename, 'w')
    context = f.read().split('\n')    
    C = int(context[0])  # C, the number of test cases
    for i in range(0,C):
        output.write( "Case #%d: %s\n"%(i+1, solve(context[i+1])))
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
