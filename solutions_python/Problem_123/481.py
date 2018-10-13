import math
import itertools

_dbg = 0


# search maximume integer'x' keeping 'func(x)' true.
def _find_mx(func, x=0, step=1):
    while True:
        assert func(x)
        nx = x + step
        if func(nx):
            x = nx
            step += step
        elif 1 == step:
            return x
        else:
            step /= 2
    

def tot(s, t):
    n = 0
    ns = s
    while ns <= t:
        ns += ns - 1
        n += 1
    return n, ns


def subsolve(s, mm):
    if 1 == s:
        return len(mm)
    if len(mm) == 0:
        return 0
    
    ts = s
    i = 0
    while i < len(mm) and ts > mm[i]:
        ts += mm[i]
        i += 1
    
    if i == len(mm):
        return 0
    
    nd = len(mm) - i
    nn, ns = tot(ts, mm[i])
    nr = subsolve(ns, mm[i:])
    return min(nd, nn + nr)

def solve(case, in_lines):
    out = 'Case #%d: '%case
 
    if _dbg:
        for line in in_lines:
            print line
            
    s, foo = [int(x) for x in in_lines[0].split()]
    mm = [int(x) for x in in_lines[1].split()]
    mm.sort()
    
    n = subsolve(s, mm)
    
#     n = 0
#     while True:
#         n1 = len(mm)
#         while n1 > 0 and s > mm[0]:
#             s += mm.pop(0)
#             n1 -= 1
#         if 0 == n1:
#             break
#         if s == 1:
#             n += n1
#             break
#         nr, sn = tot(s, mm[0])
#         c = 0
#         tsn = sn
#         while c < n1 and mm[c] < tsn:
#             tsn += mm[c]
#             c += 1
#         n2 = n1 - c + nr
#         if n2 > n1:
#             n += n1
#             break
#         else:
#             n += nr
#             s = sn

    return out+str(n)


def main(raw):
    lines = raw.split('\n')
    n = int(lines[0])
    ln = 1
    outs = []
    for case in xrange(1, n+1):
        buff = []
        endln = ln + 2
        while ln < endln and lines[ln]:
            buff.append(lines[ln])
            ln += 1
        s = solve(case, buff)
        print s
        outs.append(s)
    return '\n'.join(outs)
    pass

if __name__ == '__main__':
    test_input = """5
1 1
1
10 4
25 20 9 100
2 2
2 1
2 4
2 1 1 6
1 4
1 1 1 1"""
    force_no_file = 0
    in_file_name = '' if force_no_file else 'A-large.in'
    base_path = 'G:/workspace/py/codejam2013/R1B/'
    if in_file_name:
        with open(base_path + in_file_name) as f:
            raw = f.read()
    else:
        raw = test_input
    out = main(raw)
    if in_file_name:
        with open(base_path + in_file_name + '.out', 'w') as f:
            f.write(out)
    pass