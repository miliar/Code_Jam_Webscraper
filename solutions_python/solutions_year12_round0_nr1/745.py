# Google Code Jam 2012 qualification round A.

import sys

map = {}
def init():
    googlerese = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv q z'''
    english = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up z q'''
    for (a,b) in zip(googlerese, english):
        map[a] = b

def doCase(cyphertext):
    result = ''
    for ch in cyphertext:
        result += map[ch]
    return result

def run():
    init()
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        answer = doCase(file.readline().strip())
        print 'Case #{0}: {1}'.format(case, answer)
run()
