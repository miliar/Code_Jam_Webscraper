import sys

filename = sys.argv[1]

f = open('%s.in' % filename)
g = open('%s.out' % filename, 'w')

DEBUG = sys.argv[2] if len(sys.argv) >= 3 else False
def dlog(s, *n):
    if DEBUG:
        if n:
            print(s % tuple(n))
        else:
            print(s)

def solve(horses, roads, start, end, visited, cost=0, best=-1, curr_horse=None):
    dlog('%d %d %f %f %r %r', start, end, cost, best, curr_horse, visited)
    if start == end:
        if best == -1:
            return cost
        return min(cost, best)

    if cost > best and best > 0:
        return best

    for next_city in range(len(roads)):
        if next_city == start or next_city in visited:
            dlog("in %d, visited %d", start, next_city)
            continue

        dist = roads[start][next_city]
        if dist == -1:
            continue

        dlog('going to %d from %d on %d', next_city, start, dist)
        visited.add(next_city)

        if curr_horse and curr_horse[0] >= dist and (curr_horse[0] >= horses[start][0] or curr_horse[1] >= horses[start][1]):
            curr_horse[0] -= dist
            time = 1.0 * dist / curr_horse[1]
            best = solve(horses, roads, next_city, end, visited, cost + time, best, curr_horse)
            curr_horse[0] += dist

        if curr_horse is None or (horses[start][0] >= curr_horse[0] or horses[start][1] >= curr_horse[1]):
            curr_horse = list(horses[start])
            if curr_horse[0] >= dist:
                curr_horse[0] -= dist
                time = 1.0 * dist / curr_horse[1]
                best = solve(horses, roads, next_city, end, visited, cost + time, best, curr_horse)
                curr_horse[0] += dist

        visited.remove(next_city)

    return best

T = int(f.readline())
for t in range(T):
    dlog("Case %d", t)
    line = f.readline().strip().split()

    N = int(line[0])
    Q = int(line[1])

    horses = [0 for _ in range(N)]
    for n in range(N):
        line = f.readline().strip().split()
        endur = int(line[0])
        vel = int(line[1])
        horses[n] = (endur, vel)

    roads = []
    for n in range(N):
        line = f.readline().strip().split()
        roads.append([int(i) for i in line])

    pairs = []
    for q in range(Q):
        line = f.readline().strip().split()
        pairs.append([int(i) for i in line])

    ans = ' '.join(['%f' % solve(horses, roads, pair[0] - 1, pair[1] - 1, set()) for pair in pairs])

    g.write('Case #%d: %s' % (t + 1, ans))
    g.write('\n')


