from itertools import groupby
def count_swtich(seq):
    for i, x in enumerate(groupby(seq)):
        pass
    return i

#def solve(engines, queries):
#    freq = dict((engine, 0) for engine in engines)
#    queries = squeeze(queries)
#    for query in queries:
#        freq[query] += 1
#    if any(f==0 for f in freq.values()):
#        return 0
#    return 1
def solve(engines, queries):
    cnt = 0
    buf = set()
    for query in squeeze(queries):
        buf.add(query)
        if len(buf) == len(engines):
            cnt += 1
            buf = set([query])
    return cnt

def squeeze(seq):
    return (key for key, subgroup in groupby(seq))

def main(in_, out):
    N = int(in_.next())
    for i in range(N):
        S = int(in_.next())
        engines = [in_.next().rstrip() for j in range(S)]
        Q = int(in_.next())
        queries = [in_.next().rstrip() for j in range(Q)]
        print >>out, 'Case #%d: %d' % (i+1, solve(engines, queries))

if __name__ == '__main__':
    import sys
    main(sys.stdin, sys.stdout)
