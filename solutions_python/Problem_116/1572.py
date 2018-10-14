from collections import defaultdict


def locs(start, n, incr=1):
    "Return a list of n locations, starting at start and incrementing by incr."
    return list(range(start, start + n*incr, incr))

can_win = []
can_win += [locs(i, 4) for i in [0, 4, 8, 12]]
can_win += [locs(i, 4, 4) for i in [0, 1, 2, 3]]
can_win.append(locs(0, 4, 5))
can_win.append(locs(3, 4, 3))


def test_win(key, pos):
    if len(pos) >= 4:
        for case in can_win:
            # print key, case, pos, set(case).issubset(set(pos))
            if set(case).issubset(set(pos)):
                return True
    return False


def test_draw((key1, pos1), (key2, pos2)):
    c = 0
    for case in can_win:
        base = set(case)
        inter1 = set(pos1) & base
        inter2 = set(pos2) & base
        if len(inter1) > 0 and len(inter2) > 0:
            inter = (inter1 | inter2)
        else:
            return False
        if len(inter) > 1 and inter <= base:
            c += 1
    if c == len(can_win):
        return True
    return False


def make_map(lines):
    _map = defaultdict(list)
    j = 0
    for char in lines:
        if char == 'T':
            _map['X'].append(j)
            _map['O'].append(j)
        else:
            _map[char].append(j)
        j += 1
    return _map


def solve():
    fin = open("A-small-attempt1.in", "r")
    ##fin = open("test.txt", "r")
    fout = open("result.txt", "w")
    num_tests = int(fin.readline())

    for i in xrange(num_tests):
        test_case = ""
        for _ in range(4):
            line = fin.readline()
            test_case += line[:-1]
        fin.readline()

        _map = make_map(test_case)

        if test_win('X', _map['X']):
            fout.write("Case #%d: %s won\n" % (i+1, 'X'))
        elif test_win('O', _map['O']):
            fout.write("Case #%d: %s won\n" % (i+1, 'O'))
        else:
            if test_draw(('X', _map['X']), ('O', _map['O'])):
                fout.write("Case #%d: Draw\n" % (i+1))
            else:
                fout.write("Case #%d: Game has not completed\n" % (i+1))
    fin.close()
    fout.close()

solve()
