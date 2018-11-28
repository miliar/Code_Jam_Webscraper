# Fair-Squarem

import sys
import math

def issqr(n):
    l = 0
    u = 1
    while n >= u * u:
        u *= 2
    # invariant: sqrt(n) in xrange(l, u)
    while u - l > 1:
        m = (l + u) // 2
        if n >= m * m:
            l = m
        else:
            u = m
    return n == l * l

def is_palindrome(string):
    return string == string[::-1]


def get_result(low, high):
    i = low    
    count = 0
    
    while i <= high:
        if issqr(i) and is_palindrome(str(i)):
#                print "perfect square and palindrome %d" %(i)
                a = math.sqrt(i)
                if is_palindrome(str(int(a))):
#                    print "perfect square palindrome and even square root is palindrome %d" %(i)
                    count += 1
        i += 1        
    return count

def compute_results(inbuff, outfd):
    in_cases = int(inbuff[0])
    inbuff = inbuff[1:]
 
    for i in range(0, in_cases):
        string = inbuff[i].strip()
        low, high = string.split()
        low  = int(low)
        high = int(high)

#        print low, high 
        result = get_result(low, high)
        obuffer = "Case #%d: %d\n" %(i+1, result)
        outfd.write(obuffer)

if __name__ == "__main__":
    input = sys.argv[1]
    
    infd = open(input, "r")
    inbuff = infd.readlines()
    
    infd.close()

    outfd = open("output.txt", "w+")
    
    compute_results(inbuff, outfd)
    outfd.close()
    
