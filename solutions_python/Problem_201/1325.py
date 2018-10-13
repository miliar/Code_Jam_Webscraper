import sys
sys.setrecursionlimit(2000)

def find_my_stall(q, k):
    n = q[0]
    q.sort(reverse=True)
    q = q[1:]
    
    stall = (n+1)/2

    ls = stall - 1
    rs = n - stall

    if k == 0:
        return (max(ls, rs), min(ls, rs))
    
    if ls >= rs:
        q.append(ls)
        q.append(rs)
        return find_my_stall(q, k - 1)

    q.append(rs)
    q.append(ls)
    return find_my_stall(q, k - 1)

t = int(raw_input())
for i in xrange(1, t + 1):
    arg =  raw_input().split(" ")
    n = int(arg[0])
    k = int(arg[1])

    min_dis, max_dis = find_my_stall([n], k - 1)
    print "Case #{}: {} {}".format(i, min_dis, max_dis)
