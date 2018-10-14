import math
import itertools

def ttt(m):
    n = int(math.sqrt(m))
    if n*n == m:
        return n
    else:
        return 0

def rsame(m):
    t = str(m)
    rt = list(t)
    rt.reverse()
    t = list(t)
    return t == rt

cst = set([1, 2, 3])
def fs(hn):
    rn = hn - 1
    tpdt = 10**rn
    tp = 10**hn
    if rn >= 3:
        g3 = itertools.combinations(range(rn), 3)
        try:
            while True:
                hcde = tpdt
                item = g3.next()
                for e in item:
                    hcde += 10**e
                strh = str(hcde)[-1::-1]
                ii = int(strh)
                ee = ii + hcde * tp
                oo = ii + hcde * 10*tp
                oo1 = oo + tp
                cst.add(ee)
                cst.add(oo)
                cst.add(oo1)
        except StopIteration:
            pass
    if rn >= 2:
        g2 = itertools.combinations(range(rn), 2)
        try:
            while True:
                hcde = tpdt
                item = g2.next()
                for e in item:
                    hcde += 10**e
                strh = str(hcde)[-1::-1]
                ii = int(strh)
                ee = ii + hcde * tp
                oo = ii + hcde * 10*tp
                oo1 = oo + tp
                cst.add(ee)
                cst.add(oo)
                cst.add(oo1)
        except StopIteration:
            pass
    if rn >= 1:
        g1 = itertools.combinations(range(rn), 1)
        try:
            while True:
                hcde = tpdt
                item = g1.next()
                for e in item:
                    hcde += 10**e
                strh = str(hcde)[-1::-1]
                ii = int(strh)
                ee = ii + hcde * tp
                oo = ii + hcde * 10*tp
                oo1 = oo + tp
                oo2 = oo1 + tp
                cst.add(ee)
                cst.add(oo)
                cst.add(oo1)
                cst.add(oo2)
        except StopIteration:
            pass
    hcde = tpdt
    ii = 1
    ee = ii + hcde * tp
    eex2 = ee + ee
    oo = ii + hcde * 10*tp
    oox2 = oo + oo
    oo1 = oo + tp
    oo1x2 = oo1 + oo
    oo2 = oo1 + tp
    cst.add(ee)
    cst.add(eex2)
    cst.add(oo)
    cst.add(oox2)
    cst.add(oo1)
    cst.add(oo1x2)
    cst.add(oo2)

gl = []    
def bake():
    for n in range(1,25):
        fs(n)
    global gl
    gl = list(cst)
    gl.sort()
    gl = [x*x for x in gl]
    
def solve(case, in_lines):
    out = 'Case #%d: '%case
 
    a, b = [int(x) for x in in_lines[0].split()]
    c = 0
        
    for x in range(a, b+1):
        y = ttt(x)
        if y and rsame(x) and rsame(y):
            print x,
            c += 1

    return out + str(c)

def solve2(case, in_lines):
    out = 'Case #%d: '%case
 
    a, b = [int(x) for x in in_lines[0].split()]
    c = len([x for x in gl if b >= x >= a])
 
    return out + str(c)

def main(raw):
    bake()
    lines = raw.split('\n')
    n = int(lines[0])
    ln = 1
    outs = []
    for case in xrange(1, n+1):
        buff = []
        cl = ln + 1
        while ln < cl and lines[ln]:
            buff.append(lines[ln])
            ln += 1
        s = solve2(case, buff)
        print s
        outs.append(s)
    return '\n'.join(outs)
    pass

if __name__ == '__main__':
    test_input = """4
1 10000000
1 4
10 120
100 1000"""
    force_no_file = False
    in_file_name = '' if force_no_file else 'C-large-1.in'
    base_path = 'G:/workspace/py/codejam2013/RQ/'
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