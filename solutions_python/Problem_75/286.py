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

    data = getline().split()
    trace('data:', data)

    C = int(data[0])
    trace(C, 'combinations:')
    combinations = {}
    for combine in data[1:1+C]:
        trace('    ', combine)
        assert len(combine) == 3
        (a,b,c) = list(combine)
        combinations[a+b] = c
        combinations[b+a] = c
    trace(combinations)

    D = int(data[1+C])
    trace(D, 'oppositions:')
    oppositions = set()
    for opp in data[1+C+1:1+C+1+D]:
        trace('    ', opp)
        assert len(opp) == 2
        (a,b) = list(opp)
        oppositions.add(a+b)
        oppositions.add(b+a)
    trace(oppositions)

    N = int(data[1+C+1+D])
    trace(N, 'char string:')
    base_elements_to_invoke = data[1+C+1+D+1]
    assert len(base_elements_to_invoke) == N
    trace('    ', base_elements_to_invoke)

    element_list = []
    for base_element in base_elements_to_invoke:
        trace()
        trace('invoke base element', base_element)

        trace('  append it to list')
        element_list.append(base_element)
        trace('  element list:', element_list)

        if len(element_list) >= 2:
            # combination?:
            last_two = element_list[-2] + element_list[-1]
            result = combinations.get( last_two, None )
            if result:
                trace( '  ', last_two, 'combine to make', result )
                del element_list[-2:]
                element_list.append(result)
                trace('  element list:', element_list)
            else:
                # opposition?:
                assert element_list[-1] == base_element
                for element in element_list[:-1]:
                    if (element+base_element) in oppositions:
                        trace('  elements', element+base_element, 'in opposition')
                        element_list = []
                        trace('  element list:', element_list)
                        break

    print 'Case #%d: [%s]' % (case_num, ', '.join(element_list))
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
