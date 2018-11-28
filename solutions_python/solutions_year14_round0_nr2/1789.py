import multiprocessing 
import sys
import math
(C,F,X) = (0,0,0)
def T(x):
    result = 0.
    for i in range(0,x):
        result += 1./(2+i*F)
    result *= C
    result += X/(2+x*F)
    return result


def main():    
    tcs = int(sys.stdin.readline())
    for i in range(1, tcs+1):
        global C,F,X
        (C,F,X) = [float(x) for x in sys.stdin.readline().split()]
        pool = multiprocessing.Pool()
        _min = min(pool.map(T, range(0,int(math.ceil(X/C)))))
        print "Case #" + str(i) + ": " + str(_min)



if  __name__ =='__main__':main()
