'''
Created on 2013-04-26

@author: kai
'''
import sys
import math

def BlackAreaPaintUsed(a,radius):
    return (2*a+2*radius-1)

if __name__ == '__main__':
    
    hndlin = open(sys.argv[1],'rt')
    hndlout = open(sys.argv[2],'w')
    
    numberCases = int(hndlin.readline())
    
    
    
    for index in range(0,numberCases):
        radius, paint = hndlin.readline().rstrip('\n').split(' ')
        
        radius = float(radius)
        paint = float(paint)
        
        numberBlackRingPainted = 0
        
        index2 = 1
        while paint > 0:
            paint = paint - BlackAreaPaintUsed(index2,radius)
            if paint >= 0:
                numberBlackRingPainted +=1
                index2 = index2 + 2
            else:
                break
        
        
        
        output = "Case #"+str(index+1)+": "+ str(numberBlackRingPainted) + '\n'
        hndlout.write(output) 
    
        
    hndlin.close()
    hndlout.close()