def solve(vines, c, n, D):
    global dead_ends
    key = (c,n)
    if key in dead_ends:
        return False

    dc,lc = vines[c]
    dn,ln = vines[n]

    swing = min(dn-dc, ln)
    if D - dn <= swing:
        return True

    for i in range(n+1, len(vines)):
        dnn,lnn = vines[i]
        if dnn - dn <= swing:
            if solve(vines, n, i, D):
                return True
    dead_ends.add(key)
    return False

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        dead_ends = set()
        N = int(raw_input())
        vines = [(0,0)]
        for j in range(N):
            vines.append(map(int, raw_input().split()))
        D = int(raw_input())
        print "Case #%d:"%i,
        if solve(vines, 0, 1, D):
            print "YES"
        else:
            print "NO"

    
    
