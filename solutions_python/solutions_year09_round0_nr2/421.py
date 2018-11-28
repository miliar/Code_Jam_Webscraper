
from __future__ import print_function

def check_data(data):
    labels = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    level = map(lambda e: [None for x in e], data)
    def __check(r, c):
        if level[r][c]:
            # already visited
            return level[r][c]

        attitude = data[r][c]

        min = attitude
        next = None
        # north
        if r > 0:
            north = data[r - 1][c]
            if north < min:
                min = north
                next = (r - 1, c)
        # west
        if c > 0:
            west = data[r][c - 1]
            if west < min:
                min = west
                next = (r, c - 1)
        # east
        if c < len(data[0]) - 1:
            east = data[r][c + 1]
            if east < min:
                min = east
                next = (r, c + 1)
        # south
        if r < len(data) - 1:
            south = data[r + 1][c]
            if south < min:
                min = south
                next = (r + 1, c)
        if next:
            label = __check(next[0], next[1])
            level[r][c] = label
            return label
        else:
            # sink
            label = labels.pop(0)
            level[r][c] = label
            return label

    for r in range(len(data)):
        for c in range(len(data[0])):
            __check(r, c)
    for i in range(len(level)):
        for j in range(len(level[i])):
            print(level[i][j], end=" ")
        print()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 1:
        print("[usage] %0 [input file]" % sys.argv[0])
        sys.exit(0)

    num_cases = -1
    h = w = 0
    with open(sys.argv[1], 'r') as f:
        n = int(f.next().strip())
        for i in range(n):
            h, w = map(lambda e: int(e), f.next().strip().split())
            data = []
            for j in range(h):
                data.append([int(x) for x in f.next().strip().split()])
            print("Case #%d:" % (i+1))
            check_data(data)
