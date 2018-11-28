import fileinput
import operator
import sys

sys.setrecursionlimit(1500)

inp = fileinput.input()

forbidden = {'R': {'R', 'O', 'V'},
             'O': {'O', 'R', 'Y', 'V', 'G'},
             'Y': {'Y', 'O', 'G'},
             'G': {'G', 'Y', 'B', 'O', 'V'},
             'B': {'V', 'B', 'G'},
             'V': {'R', 'V', 'B', 'O', 'G'}}

def solve(R, O, Y, G, B, V):
    counts = {
        'R': R,
        'O': O,
        'Y': Y,
        'G': G,
        'B': B,
        'V': V,
    }


    N = sum(counts.values())
    for c in 'R', 'Y', 'B':
        if sum(counts[c1] for c1 in forbidden[c]) > N // 2:
            return "IMPOSSIBLE"



    colors = [None] * N
    i = 0

    def still_possible():
        for r,m in ('R', 'G'), ('Y', 'V'), ('B', 'O'):
            if sum(counts[c1] for c1 in forbidden[r]) > (N-i+1) // 2:
                return False

            if counts[r] < counts[m] - 1:
                return False

        return True

    if not still_possible():
        return "IMPOSSIBLE"

    colors[i] = max(counts.items(), key=operator.itemgetter(1))[0]
    counts[colors[i]] -= 1

    i = 1

    while True:
        if i == 0:
            return "IMPOSSIBLE"
        elif i == len(colors):
            if colors[-1] not in forbidden[colors[0]]:
                return ''.join(colors)
            else:
                i -= 1
        elif colors[i] is None:
            forward = False
            for c in sorted(counts.keys(), key=lambda x: (-counts[x], x)):
                if counts[c] > 0 and c not in forbidden[colors[i-1]]:
                    colors[i] = c
                    counts[c] -= 1
                    forward = True
                    break

            if forward:
                i += 1
                if not still_possible():
                    i -= 1
            else:
                i -= 1
        else:
            forward = False
            for c in sorted(counts.keys(),key=lambda x: (-counts[x], x)):
                if c > colors[i] and counts[c] > 0 and c not in forbidden[colors[i-1]]:
                    counts[colors[i]] += 1
                    colors[i] = c
                    counts[c] -= 1
                    forward = True
                    break
            if forward:
                i += 1
                if not still_possible():
                    i -= 1
            else:
                counts[colors[i]] += 1
                colors[i] = None
                i -= 1


num_cases = int(inp.readline())
for t in range(1, num_cases + 1):
    _, R, O, Y, G, B, V = (int(x) for x in inp.readline().split())
    print("Case #{}: {}".format(t, solve(R, O, Y, G, B, V)))