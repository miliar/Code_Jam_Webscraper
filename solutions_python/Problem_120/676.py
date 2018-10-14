'''
Created on 2013-4-27

@author: Martin
'''
import math

pi = math.pi;

def solution(numOfCase, c):
    resDic = {}
    for i in range(numOfCase):
        curLine = c[i+1]
        print curLine
        curLine = curLine.split()
        r = int(curLine[0])
        t = int(curLine[1])
        numOfCircle = 1
        usedPaint = 0
        while True:
            usedPaint = usedPaint + (r+2*numOfCircle-1)*(r+2*numOfCircle-1) - (r+2*numOfCircle-2)*(r+2*numOfCircle-2)
            if usedPaint > t:
                resDic[i+1] = numOfCircle-1
                print numOfCircle-1
                break
            else:
                numOfCircle = numOfCircle+1
        # end
    # end
    return resDic
            
            
if __name__ == "__main__":
    f = open("A-small-attempt0.in")
    c = f.read()
    c = c.split("\n");
    numOfCase = int(c[0])
    print numOfCase
    resDic = solution(numOfCase, c)
    for i in resDic:
        resDic[i] = "Case #" + str(i) + ": " + str(resDic[i])
    # print resDic
    f.close()
    g = open("out.out","w")
    for i in resDic:
#        if (i == numOfCase-1):
#            g.write(resDic[i])
#        else:
        g.write(resDic[i] + "\n")
    g.close