#!/usr/bin/python

import sys, math

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

def each_plan(f):
    if f==0:
        yield []
    else:
        for partial_soln in each_plan(f-1):
            yield partial_soln + [0]
            yield partial_soln + [1]

def plan_satifies_all_customers(plan):
    for types in cust_:
        for (liked_flavor,liked_maltedness) in types:
            if plan[liked_flavor-1] == liked_maltedness:
                # The plan includes a flavor+maltedness
                # that the customer likes.
                # So this customer is satisfied.
                # go to the next
                break
        else:
            # This customer is not satisfied
            return False
    return True

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    n_flavors = int(getline())
    trace(n_flavors,'flavors')
    n_custs = int(getline())
    trace(n_custs,'custs')
    cust_ = []
    for i in range(n_custs):
        trace('   cust', i)
        fields = getline().split()
        n_types_they_like = int( fields.pop(0) )
        trace('   likes', n_types_they_like, 'types')
        types = []
        for f in range(n_types_they_like):
            flavor = int(fields.pop(0))
            maltedness = int(fields.pop(0))
            trace( '       ', flavor, maltedness )
            types.append( (flavor,maltedness) )
        cust_.append(types)

    trace(cust_)

    # should at least be able to do small set with exhaustive search
    solns = []
    for plan in each_plan(n_flavors):
        n_malted = sum(plan)
        trace( plan, n_malted )
        if plan_satifies_all_customers(plan):
            trace('satisfies all')
            # This is a potential solution
            # Is it the best? (minimal malteds)
            solns.append( (n_malted, plan) )
            # if n_malted < min_so_far_malted:
        else:
            trace('does not satisfy all')

    trace(len(solns), 'solns')
    if len(solns) == 0:
        plan_str = 'IMPOSSIBLE'
    else:
        solns.sort()
        (min_malteds, best_plan) = solns[0]
        trace('soln with min malted:', min_malteds, best_plan )
        plan_str = ' '.join(map(str,best_plan))

    print 'Case #%d: %s' % (case_num, plan_str)

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
