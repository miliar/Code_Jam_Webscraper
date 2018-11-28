'''
Created on 11/4/2015

@author: user3
'''
import numpy as np

def processCase(t, n, s):
    
    cs = [int(i) for i in np.cumsum(s)]
    
    added = 0
        
    for i in range(1,n+1):
        if cs[i-1] + added < i:
            added += i - added - cs[i-1]


    return "Case #" + str(t) + ": " + str(added) + '\n'



if __name__ == '__main__':
    myinput = open('A-large.in', 'r')
    myoutput = open('A-large.out', 'w')
    
    T = int(myinput.readline())
    
    for t in range(T):
        n, s = myinput.readline().split()

        n = int(n)
        s = [int(i) for i in list(s)]
        
        res = processCase(t+1, n,s)
        myoutput.write(res)

    pass