#!/usr/bin/python

import sys, re, sets

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

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )
    print 'Case #%d:' % (case_num,)

    L = int(getline())
    trace( L, 'lines in tree')
    s = ''
    for i in range(L):
        s += getline() + ' '
    trace( 'tree text:', s ) 

    tokens = re.findall( r'\(|\)|\d+(?:\.\d+)?|[a-z]+', s )
    trace('tree tokens:', tokens)

    offset = 0
    def parse_node():
        global offset
        assert tokens[offset] == '('
        weight = float(tokens[offset+1])
        if tokens[offset+2] == ')':
            offset += 3
            return (weight,)
        else:
            feature = tokens[offset+2]
            offset += 3
            has = parse_node()
            hasnt = parse_node()
            assert tokens[offset] == ')'
            offset += 1
            return (weight, feature, has, hasnt)

    tree = parse_node()
    trace('tree:', tree)

    def decide(node, in_prob, features):
        prob = in_prob * node[0]
        if len(node) == 1:
            return prob
        elif len(node) == 4:
            if node[1] in features:
                return decide(node[2], prob, features)
            else:
                return decide(node[3], prob, features)
        else:
            assert False

    A = int(getline())
    trace( A, 'animals:')
    for i in range(A):
        fields = getline().split()
        assert len(fields) == 2 + int(fields[1])
        animal_name = fields[0]
        animal_features = sets.Set(fields[2:])
        trace( animal_name, animal_features )
        prob = decide(tree, 1, animal_features)
        print "%.7f" % prob

    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
