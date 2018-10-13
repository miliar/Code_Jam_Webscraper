T = int(raw_input())

def getsum(groupssum, a, b):
    if a<=b:
        return groupssum[b] - groupssum[a-1]
    return groupssum[b] + (groupssum[-1]-groupssum[a-1])

def getsumnum(groupssum, a, num):
    N = len(groupssum)-1
    b = ((a+num-2)%(N))+1
    return getsum(groupssum, a, b)

def getmax(groupssum, R, k, N, a):
    l = 1
    u = N
    while l < u:
        m = (l+u+1)/2
        if getsumnum(groupssum, a, m) > k:
            u = m-1
        else:
            l = m

    #print "c", l, u
    return l, getsumnum(groupssum, a, l)

for case in xrange(1, T+1):
    R, k, N = map(int, raw_input().split())
    groups = [0] + map(int, raw_input().split())
    groupssum = [0]
    for i in xrange(1,N+1):
        groupssum.append(groupssum[i-1] + groups[i])

    next = [-1]*(N+1)
    vals = [-1]*(N+1)
    cur = 1
    while next[cur] == -1:
        d, val = getmax(groupssum, R, k, N, cur)
        vals[cur] = val
        n = (cur+d-1)%N+1
        next[cur] = n
        cur = n

    #print next
    #print vals

    visited = {}
    cur = 1
    while cur not in visited:
        visited[cur] = 1
        cur = next[cur]

    loopstart = cur
    #print "loopstart", loopstart

    cur = 1
    taillen = 0
    tailcost = 0
    while cur != loopstart:
        taillen += 1
        tailcost += vals[cur]
        cur = next[cur]

    #print "taillen", taillen, "tailcost", tailcost

    cur = next[loopstart]
    looplen = 1
    loopcost = vals[loopstart]
    while cur != loopstart:
        looplen += 1
        loopcost += vals[cur]
        cur = next[cur]

    #print "looplen", looplen, "loopcost", loopcost

    if R < taillen:
        cur = 1
        ans = 0
        for i in xrange(R):
            ans += vals[cur]
            cur = next[cur]
    else:
        ans = tailcost
        R -= taillen
        ans += loopcost*(R/looplen)
        R = R%looplen
        cur = loopstart
        for i in xrange(R):
            ans += vals[cur]
            cur = next[cur]
    print "Case #%d: %d" % (case, ans)

    

