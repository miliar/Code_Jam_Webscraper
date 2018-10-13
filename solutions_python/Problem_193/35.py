import logging
from logging import debug as d
from itertools import combinations, permutations
import copy

EPS = 10 ** -6

logging.basicConfig(level=logging.DEBUG, format=('%(funcName)s(%(lineno)d):  %(message)s'))

def p(**kwargs):
    printstr = ''
    for (key, var) in kwargs.items():
        printstr += ("%s=%s\t" % (key, var))

    return printstr


def doSolve(filename, solver, log=False):
    with open(filename) as infile:
        with open(filename + ".out", 'w') as outfile:
            numCases = int(infile.readline())

            for i in range(numCases):
                inputs = parseTestCase(infile)
                print(inputs)
                result = solver(inputs)
                if log:
                    print(result)
                    print(" ")

                outfile.write("Case #%d: %s\n" % (i + 1, str(result)))


###=================================== =END TEMPLATE
# logging: d(p(varname=var, varname=var))


def parseTestCase(file):
    n = int(file.readline().strip())

    workers = []
    for i in range(n):
        w = [int(x) for x in file.readline().strip()]
        workers.append(w)

    return workers


def solver(workers):
    mgroups = []    # list of dict[set, set]

    freeworkers = []
    freemachines = [x for x in range(len(workers))]

    cost = 0

    for (w, row) in enumerate(workers):
        machines = set([])
        for (m, able) in enumerate(row):
            if able:
                machines.add(m)
                if m in freemachines:
                    freemachines.remove(m)

        # machines is all the machines 'w' can do
        if not machines:
            freeworkers.append(w)
            continue

        for groupinfo in mgroups:
            mset = groupinfo['mset']
            wset = groupinfo['wset']
            if mset & machines:
                mset |= machines
                wset.add(w)
                break
        else:
            mgroups.append({'mset': machines, 'wset': {w}})

    # Combine groups as required
    mgroups = combinegroups(mgroups)

    # Firstly, match up free workers with free machines
    for g in mgroups:
        mset = g['mset']
        wset = g['wset']
        if len(mset) > len(wset):
            if len(freeworkers) >= (len(mset) - len(wset)):
                for i in range(len(mset) - len(wset)):
                    wset.add(freeworkers.pop())
        elif len(wset) > len(mset):
            if len(freemachines) >= (len(wset) - len(mset)):
                for i in range(len(wset) - len(mset)):
                    mset.add(freemachines.pop())

    mgroups = combinegroups2(mgroups)

    # Firstly, match up free workers with free machines
    for g in mgroups:
        mset = g['mset']
        wset = g['wset']
        if len(mset) > len(wset):
            if len(freeworkers) >= (len(mset) - len(wset)):
                for i in range(len(mset) - len(wset)):
                    wset.add(freeworkers.pop())
        elif len(wset) > len(mset):
            if len(freemachines) >= (len(wset) - len(mset)):
                for i in range(len(wset) - len(mset)):
                    mset.add(freemachines.pop())

    # Go through workers and add up costs
    for (w, row) in enumerate(workers):
        if w in freeworkers:
            cost += 1
            continue

        needtoknow = getwset(w, mgroups)
        for n in needtoknow:
            if not row[n]:
                cost += 1

    return str(cost)

def getwset(w, mgroups):
    for g in mgroups:
        mset = g['mset']
        wset = g['wset']

        if w in wset:
            return mset


def combinegroups(mgroups):
    newgroups = []

    while mgroups:
        sets = mgroups.pop()
        mset = sets['mset']
        wset = sets['wset']

        keepgroups = []
        for g in mgroups:
            mset_ = g['mset']
            wset_ = g['wset']
            if mset & mset_:
                mset |= mset_
                wset |= wset_
            else:
                keepgroups.append(g)

        mgroups = keepgroups
        newgroups.append({'mset': mset, 'wset': wset})

    return newgroups

def combinegroups2(mgroups):
    newgroups = []
    keepgroups = []

    while mgroups:
        sets = mgroups.pop()
        mset = sets['mset']
        wset = sets['wset']

        if len(mset) == len(wset):
            newgroups.append(sets)
        else:
            if len(mset) > len(wset):
                sets['mcount'] = len(mset) - len(wset)
            else:
                sets['wcount'] = len(wset) - len(mset)
            keepgroups.append(sets)
    mgroups = keepgroups

    oldlen = len(mgroups)
    newlen = len(mgroups) +1
    while mgroups and oldlen != newlen and len(mgroups) > 1:
        oldlen = newlen
        sets = mgroups.pop()
        mset = sets['mset']
        wset = sets['wset']

        bestset = None
        bestval = 100
        for thisset in mgroups:
            mset_ = thisset['mset']
            wset_ = thisset['wset']

            if 'mcount' in sets and 'wcount' in thisset:
                val = sets['mcount'] + thisset['wcount']
                if val < bestval:
                    bestset = thisset
                    bestval = val
            elif 'wcount' in sets and 'mcount' in thisset:
                val = sets['wcount'] + thisset['mcount']
                if val < bestval:
                    bestset = thisset
                    bestval = val

        mgroups.remove(bestset)
        mset |= bestset['mset']
        wset |= bestset['wset']

        if len(mset) == len(wset):
            newgroups.append(sets)
        else:
            if len(mset) == len(wset):
                if 'wcount' in sets:
                    del sets['wcount']
                sets['mcount'] = len(mset) - len(wset)
            else:
                if 'mcount' in sets:
                    del sets['mcount']
                sets['wcount'] = len(wset) - len(mset)

            mgroups.append(sets)

        newlen = len(mgroups)

    return newgroups + mgroups









#FILENAME = r"test.in"
FILENAME = r"K:\downloads\D-small-attempt1.in"
doSolve(FILENAME, solver, True)
