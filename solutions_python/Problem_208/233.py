from sys import stdin

def get_time(d, sp, dists, i, d_old, sp_old):
    if i == len(dists):
        return 0
    times = []
    d_new = d[i]
    sp_new = sp[i]
    if d_new >= dists[i]:
        res1 = get_time(d, sp, dists, i + 1, d_new - dists[i], sp_new)
        if res1 is not None:
            times.append(res1 + (dists[i] + 0.0) / sp_new)
    if d_old >= dists[i]:
        res1 = get_time(d, sp, dists, i + 1, d_old - dists[i], sp_old)
        if res1 is not None:
            times.append(res1 + (dists[i] + 0.0) / sp_old)
    if len(times) == 0:
        return None
    else:
        return min(times)

def get_answer():
    parts = [int(el) for el in stdin.readline().strip().split()]
    n = parts[0]
    d = []
    sp = []
    for i in range(n):
        ps = [int(el) for el in stdin.readline().strip().split()]
        d.append(ps[0])
        sp.append(ps[1])
    dist = []
    for i in range(n):
        dist.append([int(el) for el in stdin.readline().strip().split()])
    p = stdin.readline()
    dists = []
    for line in dist[:len(dist) - 1]:
        for i in range(len(line)):
            if line[i] != -1:
                dists.append(line[i])
                break
    res = get_time(d, sp, dists, 0, 0, 0)
    return res

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print "Case #{0}: {1}".format(i + 1, get_answer())

if __name__ == "__main__":
    main()
