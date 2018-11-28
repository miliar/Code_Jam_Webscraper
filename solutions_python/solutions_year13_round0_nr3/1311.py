'''
Created on 13. apr. 2013

@author: null
'''
import math


def isPali(num):
    s = str(num)
    l = len(s)
    if l == 1:
        return True
    for i in xrange(l/2):
        if not s[i] == s[l-i-1]:
            return False
    return True
    

def checkNumber(num):
    if not isPali(num):
        return False
    rt = int(math.sqrt(num))    
    if not rt*rt == num:
        return False
    if not isPali(rt):
        return False
    return True
    

def checkGame(n,m):
    res = 0
    for i in xrange(n,m+1):
        if checkNumber(i):
            res += 1
    
    return res

if __name__ == '__main__':
    f = open("ttt1.txt")
    t = int(f.readline().strip())
    
    for i in xrange(t):
        temp1 = f.readline().strip()
        temp1 = temp1.split(" ")
        n = int(temp1[0])
        m = int(temp1[1])
            
        result = checkGame(n,m)
        
        resultString = "Case #"+ str(i+1) +": " 
        resultString += str(result)
        print resultString
    
    f.close()