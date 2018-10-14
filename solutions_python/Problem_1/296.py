import sys

def unique(l):
    return list(set(l))

def is_unique(l):
    u = {}
    for x in l:
        if x in u:
            return False
        u[x] = 1
    return True

def rm_seq_dups(l):
    ll = []
    current = None
    for i in l:
        if i != current:
            ll.append(i)
            current = i
    return ll

def longest_chain(l, max_engines):
    engines = {}
    i = 0
    while i < len(l):
        engines[l[i]] = 1
        if len(engines) > max_engines:
            break
        i += 1
    return l[:i]

def solve(ns, q):
    if len(unique(q)) < ns:
        return 0
    else:
        #qq = rm_seq_dups(q)
        i = 0
        chunks = 0
        while i < len(q):
            chunk = longest_chain(q[i:], ns - 1)
            chunks += 1
            i += len(chunk)
            #for x in chunk:
            #    print x
            #print
        return chunks - 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in xrange(n):
        ns = int(sys.stdin.readline())
        s = []
        for _ in xrange(ns):
            s.append(sys.stdin.readline().strip())
        nq = int(sys.stdin.readline())
        q = []
        for _ in xrange(nq):
            q.append(sys.stdin.readline().strip())
        min_switch = solve(len(s), q)
        print 'Case #%d: %d' % (i + 1, min_switch)
