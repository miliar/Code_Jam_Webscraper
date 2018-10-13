import sys
from math import log10

def get_digit(x,m):
    return x / m % 10

def is_tidy(x):
    m = 10**int(log10(x))
    last = x / m % 10
    curr = None
    while m > 1:
        m /= 10
        curr = x / m % 10
        if curr < last:
            return False
        last = curr
    return True

def tidy(n):
    x = 10
    y = 1
    z = 1
    mx = 10**(int(log10(n))+1)
    while x < mx:
        old = n
        while get_digit(n,x) > get_digit(n,y):
            n-=z
        if n != old:
            z*=10
        x*=10
        y*=10
        if is_tidy(n):
            break
    return n

def main():
    i = 1
    for l in sys.stdin.readlines()[1:]:
        n = int(l.strip())
        last = tidy(n)
        print "Case #{}: {}".format(i, last)
        i+=1

if __name__ == "__main__":
    main()
