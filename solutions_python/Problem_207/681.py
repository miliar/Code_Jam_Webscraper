
def valid(x, y):
    return _valid(x, y) and _valid(y, x)

def _valid(x, y):
    assert isinstance(x, str)
    assert isinstance(y, str)
    if x == y:
        return False
    if x == 'R' and y in ['O', 'V']:
        return False
    if x == 'O' and y in ['G', 'V', 'R', 'Y']:
        return False
    if x == 'Y' and y in ['O', 'G']:
        return False
    if x == 'G' and y in ['O', 'V', 'Y', 'B']:
        return False
    if x == 'B' and y in ['G', 'V']:
        return False
    if x == 'V' and y in ['O', 'G', 'R', 'B']:
        return False
    return True

def can_place(solution, color):
    if not len(solution):
        return True
    return valid(solution[-1], color)

def get_sorted(dictionary):
    itm = dictionary.items()
    itm.sort(key=lambda x: x[1], reverse=True)
    return itm

def get_sum(d1, d2):
    return sum([x[1] for x in d1.items()]) + sum([x[1] for x in d2.items()])

def solver(placed, left):
    if not len(left):
        return "".join(placed)

    elif not len(placed):
        for i in range(len(left)):
            arr = left[::]
            first = arr.pop(i)
            sol = solver([first], arr)
            if sol: return sol
    elif len(left) == 1:
        to_place = left[0]
        if valid(to_place, placed[0]) and valid(to_place, placed[-1]):
            placed.append(to_place)
            sol = solver(placed, [])
            if sol: return sol
    else:
        for i in range(len(left)):
            arr = left[::]
            to_place = arr.pop(i)
            if valid(to_place, placed[-1]):
                parr = placed[::]
                parr.append(to_place)
                sol = solver(parr, arr)
                if sol: return sol


def get_ponies(R, O, Y, G, B, V):
    ponies = []
    for i in range(R):
        ponies.append('R')
    for i in range(O):
        ponies.append('O')
    for i in range(Y):
        ponies.append('Y')
    for i in range(G):
        ponies.append('G')
    for i in range(B):
        ponies.append('B')
    for i in range(V):
        ponies.append('V')
    return ponies

def solve(r, o, y, g, b, v):
    RYB = {
        "R": r,
        "Y": y,
        "B": b
    }
    OGV = {
        "O": o,
        "G": g,
        "V": v
    }
    solution = []
    while get_sum(RYB, OGV) > 10:

        itm = get_sorted(OGV)
        placed = False
        for key, val in itm:
            if val > 0 and can_place(solution, key):
                solution.append(key)
                OGV[key] -= 1
                placed = True
                break

        if placed:
            continue

        itm = get_sorted(RYB)
        for key, val in itm:
            if val > 0 and can_place(solution, key):
                solution.append(key)
                RYB[key] -= 1
                placed = True
                break

        if not placed:
            return "IMPOSSIBLE"


    RYB.update(OGV)
    sol = solver(solution, get_ponies(**RYB))
    return sol or "IMPOSSIBLE"



with open('small.txt') as f:
    num_cases = int(f.readline())
    for i in range(num_cases):
        ponies = [int(x) for x in f.readline().strip().split(' ')]
        result = solve(*ponies[1:])
        print "Case #{}: {}".format(i + 1, result)