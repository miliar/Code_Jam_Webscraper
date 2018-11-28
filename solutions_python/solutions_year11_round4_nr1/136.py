
def solve(data):
    X, S, R, T, W = data
    table = { S : X }
    for b, e, w in W:
        d = e - b
        table[w+S] = table.get(w+S, 0) + d
        table[S] -= d

    t = 0
    for s in sorted(table.keys()):
        sec = float(table[s]) / float(s + (R - S))
        if T < sec:
            t += T + float(table[s] - (s + (R - S)) * T) / float(s)
            T = 0
        else:
            T -= sec
            t += float(table[s]) / float(s + (R - S))
    return '%.06f' % t

def get_input():
    X, S, R, t, N = map(int, raw_input().split())
    return X, S, R, t, [map(int, raw_input().split()) for i in xrange(N)]

def main():
    T = int(raw_input())
    for i in xrange(T):
        print 'Case #%d: %s' % (i + 1, solve(get_input()))

if __name__ == '__main__':
    main()
