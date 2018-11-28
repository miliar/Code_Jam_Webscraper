import sys
import math

x = 0;
n = sys.stdin.readline()
n = int(n)

while (x < n):
    x = x + 1 #count
    
    xy = sys.stdin.readline().split()
    
    counter = 0
    
    for i in range(int(xy[0]), int(xy[1]) + 1):
        le = len(str(i))
        isnotpal = 0
        ispal = 0
        
        for j in range(int(le/2)):
            if str(i)[j] != str(i)[le - j - 1]:
                isnotpal = 1
        
        if isnotpal == 0:
            isnotpal2 = 0
            sq = math.sqrt(i)
            if int(sq) == sq:
                sq = int(sq)
                le2 = len(str(sq))
                for k in range(int(le2/2)):
                    if str(sq)[k] != str(sq)[le2 - k - 1]:
                        isnotpal2 = 1
                if isnotpal2 == 0:
                    ispal = 1
                    
        if ispal == 1:
            counter = counter + 1
        
    print("Case #",x,": ", counter, sep='')