'''
Solution to Problem 1 in GCI 2012's Qualifiction Round.

(C) 2012 Aviral Dasgupta.
www.aviraldg.com
'''

mapping = {' ':' ', '\n': '\n', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def main():
    N = int(raw_input())
    for i in xrange(N):
        inp = raw_input()
        out = [mapping[c] for c in inp]
        print 'Case #{0}: {1}'.format(i+1, ''.join(out))


if __name__=='__main__':
    main()
