import sys

def is_tidy(n):
    r = n
    d = n % 10
    n = n / 10
    p = 1
    while n != 0:
        e = n % 10
        if e > d:
            return n*(10**p)
        d = e
        n = n / 10
        p += 1
    return 0

def is_tidy_(n):
    s = str(n)
    p = s[0]
    for c in s:
        if c < p:
            return False
    return True

def find_last_tidy(n):
    i = n
    while i != 0:
        x = is_tidy(i)
        if x == 0:
            return i
        i = x - 1

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(1,t+1):
        l = sys.stdin.readline()
        n = int(l)
        l = find_last_tidy(n)
        print 'Case #{}: {}'.format(i, l)

        
