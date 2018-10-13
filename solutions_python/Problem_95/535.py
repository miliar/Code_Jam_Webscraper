"""
Speaking in Tongues
https://code.google.com/codejam/contest/1460488/dashboard
"""

map = {
    ' ': ' ',
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q',
}
def main():
    T = int(raw_input())
    for t in xrange(T):
        G = raw_input().rstrip()
        ans = ''
        for c in G:
            if c in map:
                ans = ans + map[c]
        print "Case #%d: %s" % (t + 1, ans)

main()

