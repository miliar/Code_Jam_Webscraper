'''
Created on 8 avr. 2017

@author: Regis DUPUIS
'''

def isTidy(n):
    nIsTidy = True;
    
    strN = str(n)
    currentChar=0
    
    while(nIsTidy and currentChar <= len(strN)-2):
        if(strN[currentChar] > strN[currentChar+1]):
            nIsTidy = False
        else:
            currentChar += 1
    
    return nIsTidy, currentChar


def lastTidyNumber(n):
    nIsTidy, currentChar = isTidy(n)
    
    while (not nIsTidy):
        strN = list(str(n))
        
        strN[currentChar] = str( int(strN[currentChar]) - 1)
        for i in range(currentChar+1, len(strN)):
            strN[i] = "9"
        
        n= int("".join(strN))
        nIsTidy, currentChar = isTidy(n)
        
    return n


if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s = int(input())
        
        print("Case #{}: {}".format(i, lastTidyNumber(s)))
        # check out .format's specification for more formatting options