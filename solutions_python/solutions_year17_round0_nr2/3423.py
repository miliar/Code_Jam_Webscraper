import math

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = int(raw_input())
        print "Case #{}: {}".format(i, tidyNumbers(n))

def tidyNumbers(n):
    if n < 10: return n
    for i in xrange(n, 0, -1):
        if orderTest(i): return i

def orderTest(n):
    sn = str(n)
    for i in xrange(len(sn)-1):
        if sn[i] > sn[i+1]: return False
    return True

main()