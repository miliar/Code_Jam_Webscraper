import math
import itertools

_dbg = 0
    
def solve(case, in_lines):
    out = 'Case #%d: '%case
 
    if _dbg:
        for line in in_lines:
            print line
            
    r, t = [int(x) for x in in_lines[0].split()]
    
    a = 2
    b = 2 * r + 3
    c = 2 * r + 1 - t
    d = math.sqrt(b*b - 4*a*c)
    k = (d-b)/2/a
    k = int(k)
    k2 = k + 1
    k1 = k - 1
    if a*k*k + b*k + c > 0:
        k = k1
    elif a*k2*k2 + b*k2 + c <= 0:
        k = k2

    return out+str(k+1)


def main(raw):
    lines = raw.split('\n')
    n = int(lines[0])
    ln = 1
    outs = []
    for case in xrange(1, n+1):
        buff = []
        endln = ln + 1
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
1 9
1 10
3 40
1 1000000000000000000
10000000000000000 1000000000000000000"""
    force_no_file = False
    in_file_name = '' if force_no_file else 'A-small-attempt0.in'
    base_path = 'G:/workspace/py/codejam2013/R1A/'
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