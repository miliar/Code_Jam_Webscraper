import sys
import math

def read_one_int():
    return int(sys.stdin.readline().strip())

def read_line_float():
    return [float(i) for i in sys.stdin.readline().strip().split()]


N = int(sys.stdin.readline().strip())

for n in range(N):
    C, F, X = read_line_float()

    k = [0, 0]
    
    best = X/2 
    for i in range(1, math.ceil(X)):
        k[i%2]= k[(i-1)%2] + C/(2+(i-1)*F)
        
        t = k[i%2] + X/(2+i*F) 
        if t < best:
            best = t
        if t > best:
            break

    print("Case #{}: {:.6f}".format(n+1, best))

