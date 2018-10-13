import sys

def solve(qs, horses, dists):
    #print(qs, horses, dists, file=sys.stderr)

    for i in range(len(dists)):
        dists[i][i] = 0
    for i in range(len(dists)):
        for j in range(len(dists)):
            if dists[i][j] < 0:
                dists[i][j] = int(1e17)
    for k in range(len(dists)):
        for i in range(len(dists)):
            for j in range(len(dists)):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

    times = [ [1e17 if i != j else 0.0 for i in range(len(dists))] for j in range(len(dists)) ]
    for i in range(len(times)):
        for j in range(len(times)):
            if i == j:
                continue
            e,s = horses[i]
            if dists[i][j] <= e:
                times[i][j] = dists[i][j] / s

    for k in range(len(times)):
        for i in range(len(times)):
            for j in range(len(times)):
                times[i][j] = min(times[i][j], times[i][k] + times[k][j])

    ans = []
    for o,t in qs:
        ans.append(times[o-1][t-1])
    return ' '.join(str(x) for x in ans)

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    T = int(lines[0])
    i = 1
    for t in range(1,T+1):
        n, q = (int(x) for x in lines[i].split())
        i += 1
        horses = [ tuple(int(x) for x in l.split()) for l in lines[i:i+n] ]
        i += n
        dists = [ [int(x) for x in l.split()] for l in lines[i:i+n] ]
        i += n
        qs = [ tuple(int(x) for x in l.split()) for l in lines[i:i+q] ]
        i += q
        print('Case #{}: {}'.format(t, solve(qs, horses, dists)))


