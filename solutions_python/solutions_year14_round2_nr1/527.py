
def msimple(s, times):
    c = s[0]
    ntimes = 1
    for cc in s[1:]:
        if cc != c:
            yield ntimes if times else c
            c = cc
            ntimes = 1
        else:
            ntimes += 1
    yield ntimes if times else c

def diffNone(a, b):
    if a is not None and a == b:
        return a
    return None 

T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    words = [raw_input().strip() for _ in range(N)]
    wsimple = ["".join([x for x in msimple(w, False)]) for w in words]
    tsimple = [[x for x in msimple(w, True)] for w in words]
    onew = reduce(diffNone, wsimple)
    if onew is None:
        print("Case #%d: %s" % ((t+1), "Fegla Won"))
    else:
        tsimple = [list(x) for x in zip(*tsimple)]
        tmean = [float(sum(x))/float(len(x)) for x in tsimple]
        displ = 0
        for vec, mean in zip(tsimple, tmean):
            mean = int(mean + .5)
            displ += sum([abs(x-mean) for x in vec])
        print("Case #%d: %d" % ((t+1), displ))
        
