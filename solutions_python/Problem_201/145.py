#!/usr/bin/python

def smart(n, k):
    a = 1
    while a * 2 - 1 < k:
        a *= 2
    
    total = n - a + 1
    low = total // a
    num_highs = total - low * a
    
    if k - a < num_highs:
        s = low + 1
    else:
        s = low
        
    min_s = (s - 1) // 2
    max_s = (s - 1) - min_s
    
    return max_s, min_s

T = int(raw_input())
for t in range(T):
    N, K = map(int, raw_input().split())
    
    a, b = smart(N, K)
    print "Case #%d: %d %d" % (t + 1, a, b)