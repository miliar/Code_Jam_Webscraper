import numpy as np


def  get_s1(a,b,n):
    i = 0
    s1 = 0
    for j in range(n):
        while i < n:
            if a[i] > b[j]:
                s1 += 1
                break
            i += 1
        i += 1
    return s1

def get_s2(a,b,n):
    s2 = 0
    j = 0
    for i in range(n):
        while j < n:
            if b[j] > a[i]:
                s2 += 1
                j += 1
                break
            j += 1
    return n - s2    

T = int(raw_input())
for  i in range(T):
    n = int(raw_input())
    a = map(float,raw_input().split())
    b = map(float,raw_input().split())

    a = np.array(a)
    a.sort()
    b = np.array(b)
    b.sort()
    
    s1 = get_s1(a,b,n)
    s2 = get_s2(a,b,n)
    
    print "Case #%s: %d %d" % (str(i+1), s1, s2)