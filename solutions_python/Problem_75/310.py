import sys

f = map(str.strip, open(sys.argv[1], 'rb').readlines(), "\n")
n = int(f.pop(0))

def solve(c, d, q):
    out = ""
    for i in q:
        out += i
        while ''.join(sorted(out[-2:])) in c.keys():
            out = out[:-2] + c[''.join(sorted(out[-2:]))]
        for j in d:
            if j[0] in out and j[1] in out:
                out = ""
    return out

for i in range(n):
    l = f[i].split()
    comb = {''.join(sorted(x[:2])):x[2] for x in l[1:int(l[0]) + 1]}
    cn = len(comb) + 2
    dest = l[cn : cn + int(l[cn - 1])]
    dn = len(dest)
    queue = l[-1]
    print "Case #%s: [%s]" % (i+1, ', '.join(solve(comb, dest, queue)))
