import fileinput
import math

def get_val(f, t=int):
    v = f.readline().strip()
    if t:
        v = t(v)
    return v

def get_line(f, t=int):
    v = f.readline().strip().split()
    if t:
        v = [t(x) for x in v]
    return v

with fileinput.input() as f:
    for case in range(get_val(f)):
        N, K = get_line(f)
        U = get_val(f, float)
        ps = get_line(f, float)
        ps.sort()
        ps = ps + [1.0]
        multiple = 1
        low = ps[0]
        for i in range(len(ps) -1):
            gap = ps[i + 1] - ps[i]
            pour = min(U, gap * multiple)
            U -= pour
            low += pour / multiple
            multiple += 1
        result = 1.0
        for p in ps:
            result *= max(low, p)
        print("Case #{}: {}".format(case + 1, result))
