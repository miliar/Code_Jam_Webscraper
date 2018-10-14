import sys

def main():
    inp = sys.stdin
    T = int(inp.readline())
    for t in xrange(T):
        N, M = map(int, inp.readline().strip().split())
        existing = []
        for _ in xrange(N):
            existing.append(inp.readline().strip())
        needed = []
        for _ in xrange(M):
            needed.append(inp.readline().strip())
        existing.append("")
        existing = sorted(map(lambda x:tuple(x.split('/')), existing))
        existing_s = set(existing)
        needed = sorted(map(lambda x:tuple(x.split('/')), needed))
        res = 0
        for n in needed:
            for p in xrange(1, len(n)+1):
                if n[:p] not in existing_s:
                    res += 1
                    existing_s.add(n[:p])
        print "Case #%d: %d" % (t+1, res)

main()
