import codejam as gcj
import codejam.datastructures as dst

def cost(o, e):
    return sum(N - i for i in range(e - o))

T = gcj.read_input('i')
for t in range(T):
    N, M, J = gcj.read_input('i i->', 'i i i')
    starts, ends, points = dst.defaultdict(int), dst.defaultdict(int), []
    simple = []
    full_cost, min_cost = 0, 0

    for o, e, p in J:
        points += [o, e]
        starts[o] += p
        ends[e] += p
        full_cost += p * cost(o, e)
    points = sorted(set(points))

    blocks = []
    h = 0
    for i, x in enumerate(points[:-1]):
        h += (starts[x] - ends[x])
        blocks += [[points[i + 1] - x, h]]
    blocks += [[0, 0]]

    while blocks != []:
        dist, height = 0, 10**10
        for i, (d, h) in enumerate(blocks):
            if h == 0:
                min_cost += height * cost(0, dist)
                for j in range(i):
                    blocks[j][1] -= height
                break
            else:
                height = min(height, h)
                dist += d

        while blocks != [] and blocks[0][1] == 0:
            blocks.pop(0)

    print 'Case #%i:' % (t + 1), (full_cost - min_cost) % 1000002013