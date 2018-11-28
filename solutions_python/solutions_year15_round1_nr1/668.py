T = int(raw_input())

def min_speed(M):
    s = 0
    for i in range(0, len(M)-1):
        if M[i] - M[i+1] > 0:
            s = max(s, M[i] - M[i+1])
    return s

def first_method(M):
    n = 0
    for i in range(0, len(M)-1):
        if M[i] - M[i+1] > 0:
            n += M[i] - M[i+1]
    return n

def second_method(M, s):
    n = 0
    for i in range(0, len(M)-1):
        n += min(s, M[i])
    return n
    
for t in range(1, T+1):
    N = int(raw_input())
    M = [int(m) for m in raw_input().split()]
    n1 = first_method(M)
    s = min_speed(M)
    n2 = second_method(M, s)
    print "Case #%d: %d %d" % (t, n1, n2)
