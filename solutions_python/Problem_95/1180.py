#!/usr/bin/python

import sys, string

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

class Bunch:
    def __init__( self, **kwds ):
        self.__dict__ = kwds

pause_after_trace = False
def trace(*strs):
    f = sys.stderr
    print >> f, '..',
    for str in strs:
        print >> f, str,
    print >> f
    if pause_after_trace:
        response = raw_goo('? ')
        if response == 'q':
            sys.exit(1)

goo = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
'''

eng = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
'''

assert len(goo) == len(eng)

g_to_e = {
    'y': 'a',
    'e': 'o',
    'q': 'z',
}
for (g, e) in zip(goo, eng):
    # print g, e
    if g in g_to_e:
        assert e == g_to_e[g], g_to_e[g]
    else:
        g_to_e[g] = e

all_letters = set(string.lowercase)
missing_g_letter = (all_letters - set(g_to_e.keys())).pop()
missing_e_letter = (all_letters - set(g_to_e.values())).pop()

# print missing_g_letter, missing_e_letter
g_to_e[missing_g_letter] = missing_e_letter

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    goo_line = getline()
    eng_line = ''.join(g_to_e[g] for g in goo_line)

    print 'Case #%d: %s' % (case_num, eng_line)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
