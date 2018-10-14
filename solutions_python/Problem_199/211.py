import sys

def main():
    with open(sys.argv[1]) as f, open(sys.argv[1] + '.out', 'w') as out:
        T = int(next(f))
        for i in xrange(T):
            state, size = next(f).split()
            size = int(size)
            out.write('Case #%d: %s\n' % (i + 1, count(state, size)))

def count(state, size):
    i = 0
    n = 0
    state = [1 if x == '+' else -1 for x in state]
    while i < len(state) - size:
        if state[i] == -1:
            for j in xrange(i, i + size):
                state[j] *= -1
            n += 1
        i += 1
    if state[i] == 1 and all(x == 1 for x in state[i+1:]):
        return str(n)
    elif state[i] == -1 and all(x == -1 for x in state[i+1:]):
        return str(n + 1)
    return 'IMPOSSIBLE'

if __name__ == '__main__':
    main()
