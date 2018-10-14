if __name__ == '__main__':
    import string, sys

    mapping_n2g = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 
            'd': 'i',
            'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u',
            'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd',
            'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a',
            'x': 'h',
            'q': 'z', 'z': 'q'}

    mapping_g2n = {}
    for k, v in mapping_n2g.items():
        mapping_g2n[v] = k

    T = int(sys.stdin.readline())

    for i in xrange(T):
        G = sys.stdin.readline().strip()
        S = [mapping_g2n[letter] for letter in G]
        print "Case #%d: %s" % (i+1, "".join(S))
