def parse(u):
    ret = [u]
    pos = u.find("/", 1)
    while pos != -1:
        ret.append(u[:pos])
        pos = u.find("/", pos+1)
    return set(ret)

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        N, M = map(int, raw_input().split())
        lst = set()
        lstnew = set()
        for i in range(N):
            u = raw_input()
            lst |= parse(u)
        for i in range(M):
            u = raw_input()
            lstnew |= parse(u)
        #print "old", lst
        #print "new", lstnew
        
        lst = set(lst)
        lstnew = set(lstnew)
        print "Case #%d: %d" % (t+1, len(lstnew - lst))
        