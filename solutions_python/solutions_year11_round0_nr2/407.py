#!/usr/bin/python -u

import sys, re

#----------------------------------------------------------------------
def solve(combiningElements, opposingElements, elementsToInvoke):

    state = []

    while elementsToInvoke:

        # print "invoking",elementsToInvoke[0]

        state.append(elementsToInvoke.pop(0))

        if len(state) < 2:
            continue

        # check for combinations at the end
        key = "".join(state[-2:])

        result = combiningElements.get(key,None)

        if result != None:
            state.pop(-1)
            state.pop(-1)
            state.append(result)

            # most likely, if the new result opposes something
            # already in the list, this is NOT counted as
            # invocation, i.e. the list is NOT cleared...

            continue

        # check for opposition

        # get opposing elements for newly inserted element
        
        opposing = opposingElements.get(state[-1],None)
        if opposing == None:
            continue
        
        for opp in opposing:
            # note: could probably be made more efficient here but sufficient
            # for the problem size
            if opp in state[:-1]:
                state = []
                break

    return state

#----------------------------------------------------------------------
# main
#----------------------------------------------------------------------

T = int(sys.stdin.readline())

for case in range(1,T+1):

    items = re.split('\s+',sys.stdin.readline().split('\n')[0])

    C = int(items.pop(0))

    # maps from pair of base elements to product
    baseElementsRules = {}

    for x in range(C):
        rule = items.pop(0)

        baseElements = rule[:2]
        nonBaseElement = rule[2]

        # add both pairs
        baseElementsRules[ baseElements[0] + baseElements[1]] = nonBaseElement
        baseElementsRules[ baseElements[1] + baseElements[0]] = nonBaseElement

    #--------------------
    # read opposing base elements
    #--------------------
    D = int(items.pop(0))

    # maps from one member of the pair to list of others
    opposingElements = {}

    for x in range(D):
        rule = items.pop(0)

        baseElements = rule[:2]

        # add both pairs
        opposingElements.setdefault(baseElements[0],set()).add(baseElements[1])
        opposingElements.setdefault(baseElements[1],set()).add(baseElements[0])        

    # print "HERE"

    #--------------------    
    N = int(items.pop(0))

    elementsToInvoke = items.pop(0)

    if len(elementsToInvoke) != N:
        print >> sys.stderr,"warning: string length does not match"

    elementsToInvoke = list(elementsToInvoke)

    sol = solve(baseElementsRules, opposingElements, elementsToInvoke)

    print "Case #%d:" %case,"[" + ", ".join(sol) + "]"
