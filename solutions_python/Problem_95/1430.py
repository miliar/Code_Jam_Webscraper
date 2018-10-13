import sys

D = open('/usr/share/dict/cracklib-small', 'r').readlines()
D = [d.strip() for d in D]



WORDS = set()

            #print WORDS

import string

BASE = {}
LETTERS = set()
for x in string.letters:
    #BASE[string.lower(x)] = None
    LETTERS.add(string.lower(x))


BASE['a'] = 'y'
BASE['o'] = 'e'
BASE['z'] = 'q'

BASE = {
    'a' : 'y',
    'o' : 'e',
    'z' : 'q',
    'b' : None,
    'c' : None,
    'd' : None,
    'e' : None,
    'f' : None,
    'g' : None,
    'h' : None,
    'i' : None,
    'j' : None,
    'k' : None,
    'l' : None,
    'm' : None,
    'p' : None,
    'q' : None,
    'r' : None,
    's' : None,
    't' : None,
    'u' : None,
    'v' : None,
    'w' : None,
    'x' : None,
    'y' : None,
}


BASE = {
    'y' : 'a',
    'e' : 'o',
    'q' : 'z',
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'z' : 'q',
}



r, s = [], []
for k, v in BASE.items():

    if v != None:
        r.append(k)
    if v != None:
        LETTERS.remove(v)

        #print "BOUND,     ", ''.join(sorted(r))
        #print 'REMAINING, ', ''.join(sorted(list(LETTERS)))


lines = list(enumerate(sys.stdin.readlines()[1:]))

from collections import defaultdict
two = defaultdict(int)
for i,l in lines:
    for w in l.strip().split(' '):
        if len(w) == 2:
            two[w] += 1
            #for k,v in sorted(two.items(), key = lambda x: -x[1])[:10]:
    #print k, v


for i,l in lines:
    l = l.strip()
    r = []
    for c in l:
        if BASE.has_key(c) and BASE[c]:
            r.append(BASE[c])
        else:
            r.append(c)
    r = ''.join(r)
    print 'Case #%s: %s' % (i+1,r)







"""
def validate(mapping):
    s = set(mapping.values())
    if None in s:
        s.remove(None)
    assert len([x for x in mapping.values() if x]) == len(s)

validate(BASE)


def fix_word(mapping, word):
    values = set(mapping.values())
    for w in word:
        if w in values


print BASE
"""

"""
        print "Case #%s:" % str(nn)
        for i in range(teams):
            print 0.25 * WPS[i] + 0.50 * OWPS[i] + 0.25 * OOWP[i]

            """