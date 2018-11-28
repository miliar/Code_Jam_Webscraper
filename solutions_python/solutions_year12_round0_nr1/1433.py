def solve(i):
    # Obtained from the problem description and examples.
    # See get_translation.py.
    t = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v',
         'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g',
         'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j',
         't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
    return ''.join(t[c] for c in i)

if __name__ == '__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        s = solve(raw_input())
        print 'Case #%d: %s' % (i, s)
