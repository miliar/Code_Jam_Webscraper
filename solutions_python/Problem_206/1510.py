'''
Created on 22 avr. 2017

@author: Regis DUPUIS
'''


if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    t = int(input())  # read a line with a single integer
    
    numTestCases = 0;
    while(numTestCases < t):
        d, n = [int(s) for s in input().split(" ")]
        
        tMax = None
        for otherHorses in range(1, n + 1):
            ki, si = [int(s) for s in input().split(" ")]
            ti = (d-ki)/si
            if tMax==None or ti>tMax :
                tMax=ti
        
        s = d/tMax
        numTestCases += 1
        
        print("Case #{}: {}".format(numTestCases, s))
        # check out .format's specification for more formatting options