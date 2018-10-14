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
        ps = []
        for n in range(N):
            ps.append(get_line(f))
        ps.sort(key=lambda x: x[0], reverse=True)
        results = []
        for r, h in ps:
            results = [(result[0] + 2 * math.pi * r * h, result[1] + 1) for result in results] + results
            results.append((math.pi * r**2 + 2 * math.pi * r * h, 1))
        results = [result[0] for result in results if result[1] == K]
        results.sort()
        result = results[-1]
        print("Case #{}: {}".format(case + 1, result))
