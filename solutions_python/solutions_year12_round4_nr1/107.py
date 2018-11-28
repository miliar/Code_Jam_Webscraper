import sys

__author__ = 'joranvar'


def solve(case):
    vines = case[:-1]
    ledge = case[-1]

    def swing(pos, vine):
        if len(vine) > 2 and vine[2] < pos:
            # Have swung this vine before, with a wider reach
            return False

        if len(vine) == 3:
            vine[2] = pos
        else:
            vine.append(pos)

        if pos + (2*(vine[0] - pos)) >= ledge:
            return True

        # Which vines can I reach?
        reachable = [v for v in vines if vine[0] < v[0] <= pos + (2*(vine[0] - pos))]

        # Swing every vine in reach
        for v in reachable:
            # Climb
            pos = max(vine[0], v[0] - v[1])

            if swing(pos, v):
                return True
        return False

    vine = vines[0]
    pos = 0

    # Swing
    if swing(pos, vine):
        return 'YES\n'
    else:
        return 'NO\n'

if __name__ == "__main__":
    fi = open('a.in')

    T = int(fi.readline())
    cases = []
    for t in range(T):
        N = int(fi.readline())
        cases.append([])
        for n in range(N):
            cases[-1].append(list(map(int, fi.readline().split(' '))))
        cases[-1].append(int(fi.readline()))

    G = [s for s in map(solve, cases)]

    fo = open('a.out', 'w')
    fo.writelines(['Case #' + str(i) + ': ' + l for i, l in enumerate(G,1)])

    fo.flush()
    fo.close()