
def check_point(x, y, H, W, table, value):
    if 0 <= x < H and 0 <= y < W:
        return table[x][y] < value
    return False

def find_sink(point, H, W, table, answer, symbol):
    x, y = point
    min_point = (x, y)
    min_value = table[x][y]
    for i, j in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        if check_point(x + i, y + j, H, W, table, min_value):
            min_point = (x + i, y + j)
            min_value = table[x + i][y + j]

    i, j = min_point
    if (i, j) == (x, y):
        # sink
        if answer[i][j] is None:
            answer[i][j] = symbol
        return i, j
    else:
        if answer[i][j] is None:
            sink = find_sink((i, j), H, W, table, answer, symbol)
        else:
            sink = (i, j)
        answer[x][y] = answer[sink[0]][sink[1]]
        return sink

def main():
    T = int(raw_input())

    for case in xrange(T):
        H, W = map(int, raw_input().split())
        table = []
        answer = []

        for h in xrange(H):
            table.append(map(int, raw_input().split()))
            assert(len(table[-1]) == W)
            answer.append([None for i in xrange(W)])

        sym = ord('a')
        for i in xrange(H):
            for j in xrange(W):
                if answer[i][j] is None:
                    find_sink((i, j), H, W, table, answer, chr(sym))
                    if answer[i][j] == chr(sym):
                        sym += 1

        print 'Case #%d:' % (case + 1)
        for i in xrange(H):
            print ' '.join(answer[i])

if __name__ == '__main__':
    main()