import sys

def next_perm(a, n):
    j = n - 2
    while j > 0 and a[j] >= a[j+1]:
        j -= 1

    m = n - 1
    while m > j and a[m] <= a[j]:
        m -= 1

    a[j], a[m] = a[m], a[j]

    def reverse(a, start, end):
        pos = 0
        while start + pos < end - pos:
            a[start + pos], a[end - pos] = a[end - pos], a[start + pos]
            pos += 1

    reverse(a, j+1, n-1)

def fact(x):
    ret = 1
    for i in range(1,x+1):
        ret *= i
    return ret

inp = open(sys.argv[1])
lines = inp.readlines()
inp.close()

N = int(lines[0])


def calc(to_r,ln):
    arr = [1] * ln
    ret = 0

    for i in to_r:
        arr[i] = 0
        left = i - 1
        right = i + 1
        while left > 0 and arr[left] != 0:
            ret += 1
            left -= 1
        while right < ln  and arr[right] != 0:
            ret += 1
            right += 1
    return ret
        
    
for i in range(0, N):
    P, Q = map(int,lines[i*2+1].split(' '))
    to_r = map(int, lines[i*2+2].split(' '))
    to_r.sort()

    perms = fact(Q)
    ret = 1000000000
    while perms:
        ret = min(ret,calc(to_r,P+1))
        next_perm(to_r,len(to_r))
        perms -= 1
    print "Case #%d:" % (i + 1), ret
        
        



    
