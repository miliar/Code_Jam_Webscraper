
def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret


def valid(i, j, MAP):
    n = len(MAP)
    m = len(MAP[0])
    return 0 <= i < n and 0 <= j < m


def caught(MAP, r, c, d):
    dmap = {"<": (0, -1),
            ">": (0, 1),
            "^": (-1, 0),
            "v": (1, 0)}
    di, dj = dmap[d]
    i, j = r + di, c + dj
    while valid(i, j, MAP):
        if MAP[i][j] != '.':
            return True
        i, j = i + di, j + dj
    return False


def main():
    for T in range(1, 1+input()):
        R, C = read_array(int)
        MAP = [raw_input() for _ in range(R)]
        ans = 0
        ok = True
        for r in range(R):
            for c in range(C):
                grid = MAP[r][c]
                if grid == '.':
                    continue
                else:
                    if caught(MAP, r, c, grid):
                        continue
                    else:
                        be_caught = False
                        for d in "<>^v":
                            if caught(MAP, r, c, d):
                                be_caught = True
                                break
                        if be_caught:
                            ans += 1
                        else:
                            ok = False
                            break

        print "Case #%d: %s" % (T, ok and str(ans) or "IMPOSSIBLE")


main()
