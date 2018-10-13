import sys

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

def process(l,h,num):
    found = False
    for n in range(l,h+1):
        ctr = 0
        for nn in num:
            if nn % n == 0 or n % nn == 0:
                ctr += 1
            else:
                break
        if ctr == len(num):
            return n
        
    if not found:
        return "NO"

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for tt in range(0,t):
        n,l,h = sys.stdin.readline().strip().split()
        l = int(l)
        h = int(h)
        num = map(int,sys.stdin.readline().strip().split())
        print "Case #%i: %s" %  (tt+1,process(l,h,num))

    
