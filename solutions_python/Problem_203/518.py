import random
from copy import deepcopy
from collections import defaultdict

def valid_cake(cake):
    if not all('?' not in row for row in cake):
        return False


def neighbours(cake, x, y):
    n = set()
    for dx, dy in {(0, -1), (0, 1), (-1, 0), (1, 0)}:
        try:
            n.add(cake[y+dy][x+dx])
        except:
            pass

    return n


def cont_rec(s):
    if len(s) == 1:
        return True

    tl = (min(a[0] for a in s), min(a[1] for a in s))
    br = (max(a[0] for a in s), max(a[1] for a in s))

    disconts = set()

    for y in range(tl[1], br[1] + 1):
        for x in range(tl[0], br[0] + 1):
            if (x, y) not in s:
                disconts.add((x, y))

    if len(disconts) == 0:
        return True
    else:
        return disconts



for case in range(1, int(input()) + 1):
    res = None

    r, c = (int(x) for x in input().split())
    cake = []

    for _ in range(r):
        row = input().strip()
        cake.append(list(row))

    INITIAL_CAKE = deepcopy(cake)

    loops = 0

    while (any('?' in row for row in cake)):
        locs = defaultdict(list)

        for y in range(len(cake)):
            for x in range(len(cake[0])):
                locs[cake[y][x]].append((x, y))

        ###
        if '?' not in locs:
            print("Case #{}:".format(case))
            for line in cake:
                print(''.join(line))
            break
        ##


        # Check for disconts
        for k, v in locs.items():
            if k == '?':
                continue

            if cont_rec(v) != True:
                tl = min(v)
                br = max(v)

                for y in range(tl[1], br[1] + 1):
                    for x in range(tl[0], br[0] + 1):
                        # Reassign blanks
                        cake[y][x] = k
                        if (x, y) in locs['?']:
                            locs['?'].remove((x, y))

                break

        else:
            # fill random question mark
            qs = list(locs['?'])
            random.shuffle(qs)
            if not qs:
                continue

            for x, y in qs:
                neighs = neighbours(cake, x, y)
                gottem = False
                for t in neighs:
                    if t == '?':
                        continue

                    nl = locs[t][:]
                    nl.append((x, y))
                    cont = cont_rec(nl)

                    if cont == True:
                        cake[y][x] = t
                        gottem = True
                        break

                    else:
                        if all(cake[b][a] == '?' for a, b in cont):
                            cake[y][x] = t
                            for (a, b) in cont:
                                cake[b][a] = t
                            gottem = True
                            break



                if gottem:
                    break

        loops += 1

        if loops > r * c:
            cake = deepcopy(INITIAL_CAKE)
            loops = 0

    print("Case #{}:".format(case))
    for line in cake:
        print(''.join(line))

