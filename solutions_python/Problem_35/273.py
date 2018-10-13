import itertools
def neighbours(i, j, h, w) :
    n = []
    if i > 0 : n.append((i - 1, j)) # North
    if j > 0 : n.append((i, j - 1)) # West
    if j < w - 1 : n.append((i, j + 1)) # East
    if i < h - 1 : n.append((i + 1, j)) # South

    return n

with open('B-large.in') as file :
    num_test_cases = int(file.readline())
    for test_case in range(num_test_cases) :
        h, w = map(int, file.readline().split())
        x = [[int(i) for i in file.readline().split()] for j in range(h)]
        alt = {(i, j) : x[i][j] for i, j in itertools.product(range(h), range(w))}
        basins = {}
        coords = list(itertools.product(range(h), range(w)))
        next_basin = ord('a')
        while coords :
            chain = []
            x, y = coords.pop(0)
            while True :
                if (x, y) in basins :
                    for i in chain :
                        basins[i] = basins[x, y]
                    break

                chain.append((x, y))
                n = neighbours(x, y, h, w)
                if n :
                    a = [alt[i] for i in n]
                    m = min(a)
                else :
                    m = -1
                if m >= alt[x, y] or m == -1:
                    if (x, y) in basins :
                        for i in chain :
                            basins[i] = basins[x, y]
                        break
                    for i in chain :
                        basins[i] = chr(next_basin)

                    next_basin += 1
                else :
                    x, y = n[a.index(m)]

        print('Case #{}:'.format(test_case + 1))
        for i in range(h) :
            for j in range(w) :
                print(basins[i, j], end = ' ')
            print()


