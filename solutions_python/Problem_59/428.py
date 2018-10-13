#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    return
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

def memoize(f):
    memos = {}
    def memoized_f( *args ):
        try:
            result = memos[args]
            trace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            trace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    wanted_paths = []

    (N,M) = map(int,getline().split())

    n_mkdirs = 0
    counting_mkdirs = False

    def insert(tree,path):
        if path == []: return
        (head,tail) = (path[0],path[1:])
        if head in tree:
            subtree = tree[head]
        else:
            subtree = {}
            if counting_mkdirs:
                trace('mkdir', head)
                global n_mkdirs
                n_mkdirs += 1
            tree[head] = subtree
        insert(subtree,tail)

    tree = {}

    trace(N,'existing paths:')
    for i in range(N):
        path = getline().split('/')[1:]
        trace(path)
        insert(tree,path)

    trace('tree:')
    # import pprint; pprint.pprint(tree)

    trace(M,'wanted paths:')
    counting_mkdirs = True
    for i in range(M):
        path = getline().split('/')[1:]
        trace(path)
        insert(tree,path)
        # pprint.pprint(tree)

    print 'Case #%d: %s' % (case_num, n_mkdirs)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
