import sys

def main():
    with open(sys.argv[1]) as f, open(sys.argv[1] + '.out', 'w') as out:
        T = int(next(f))
        for i in xrange(T):
            out.write('Case #%d: %s\n' % (i + 1, lastTidy(next(f).strip())))

def lastTidy(N):
    N = map(int, N)
    start = i = 0
    while i < len(N) - 1:
        if N[i] == N[i+1]:
            i += 1
        elif N[i] < N[i+1]:
            i += 1
            start = i
        else:
            N[start] -= 1
            for j in xrange(start+1, len(N)):
                N[j] = 9
            if N[start] == 0:
                N = N[start+1:]
    return ''.join(map(str, N))

if __name__ == '__main__':
    main()
