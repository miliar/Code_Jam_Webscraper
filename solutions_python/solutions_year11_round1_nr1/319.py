import sys
import math

def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result

for k in range(1, int(sys.stdin.readline())+1):
    line = sys.stdin.readline().rstrip().split()
    
    N = int(line[0])
    pd = int(line[1])
    pg = int(line[2])
    

    #print line
    if not (pg == 100 and pd < 100):
        
        if pg == 0 and pd <> 0:
            print "Case #%d: Broken"%k
            continue                   
        
        if N <= 100:
            ff = 1
            for j in range(1,N+1):
                tmp = pd/100.0*j
                #print k, N, j, pd, tmp
                if math.floor(tmp) == tmp:
                    #print 'Buuuuut ',math.floor(tmp)
                    print "Case #%d: Possible"%k
                    ff = 0
                    break
    
            if ff:
                print "Case #%d: Broken"%k
        else:
            print "Case #%d: Possible"%k
    else:
        print "Case #%d: Broken"%k
            