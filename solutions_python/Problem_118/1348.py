'''
Created on 2013-4-14

@author: Martin
'''
import math

def isPal(s):
    l = len(s)
    left = 0
    right = l-1
    while True:
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        left = left+1
        right = right-1
    # end while
        
        
def solution(numOfCase, c):
    resDic = {}
    for i in range(numOfCase):
        cur = c[i+1].split()
        start = int(cur[0])
        to = int(cur[1])
        count = 0
        for j in range(start, to+1):
            if isPal(str(j))==True and (math.floor(math.sqrt(j)) * math.floor(math.sqrt(j)))==j:
                if isPal(str(int(math.sqrt(j))))==True:
#                    print j
                    count = count + 1
        resDic[i] = count
    return resDic
    
if __name__ == "__main__":
    f = open("C-small-attempt1.in")
    c = f.read()
    c = c.split("\n");
    numOfCase = int(c[0])
#    print numOfCase
    resDic = solution(numOfCase, c)
    f.close()
    g = open("C.out","w")
    for i in resDic:
        if i==numOfCase-1:
            g.write("Case #"+str(i+1) + ": " + str(resDic[i]))
        else:
            g.write("Case #"+str(i+1) + ": " + str(resDic[i]) + "\n")
    g.close()