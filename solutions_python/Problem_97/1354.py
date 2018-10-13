#! pypy
def recycled(n, minn, maxn):
    s = str(n)
    return len(set([int(s[i:]+s[:i]) for i in range(1, len(s)) if (n < int(s[i:]+s[:i]) <= maxn)]))

f = open("clarge.in", "r")
l = map(lambda x: x.strip(), f.readlines())

cnt = 1
ans = 0
N = int(l[0])
for st in l[1:]:
    if len(st.strip()) == 0:
        break
    print "Case #%d:" % cnt,
    cnt += 1
    a, b = map(lambda x: int(x), st.split())

    ans = sum([recycled(i, a, b) for i in range(a, b+1)])
    print ans



