#! /usr/bin/python

__author__ = 'Thomas "noio" van den Berg'

### IMPORTS ###
import sys
import numpy as np
from pprint import pprint

calls = 0

### FUNCTIONS ###    
def coll(sets):
    changed = True
    while changed:
        sets = list(set(frozenset(s) for s in sets))
        changed = False
        for seta in sets:
            for setb in sets:
                if seta != setb:
                    if seta & setb:
                        sets.remove(seta)
                        sets.remove(setb)
                        sets.append(seta | setb)
                        changed = True
                        break
    return sets


def och(chests, keys, order=[]):
    """ recursively open a chest with a key 
        return order if last chest was opened.
    """
    global calls
    calls += 1

    # base case last chest
    if len(chests) == 0:
        return order
    # base case no keys
    if len(keys) == 0:
        return None

    needed = np.zeros((201))
    fc = np.bincount([c[0] for c in chests])
    needed[:len(fc)] += fc
    have = np.bincount(keys)
    needed[:len(have)] -= have
    canget = [k for chest in chests for k in chest[2]]
    if canget:
        canget = np.bincount(canget)
        needed[:len(canget)] -= canget
    
    if any(needed > 0):
        return None
    

    for chest in chests:
        if chest[0] in keys:
            nch = chests[:]
            nch.remove(chest)
            nks = keys[:]
            nks.remove(chest[0])
            nks.extend(chest[2])
            sol = och(nch, nks, order + [chest[1]])
            if sol is not None:
                return sol

    return None

def do(keys, chests):
    # Chests are (key, index, content)
    chests = [(chest[0], i+1, chest[2:]) for i, chest in enumerate(chests)]
    keys = sorted(keys)

    sets = [set([chest[0]] + chest[2]) for chest in chests]
    sets = coll(sets)

    print "CHESTS"
    pprint(chests)
    chestgroups = [ [] for _ in xrange(len(sets)) ]
    keygroups = [ [] for _ in xrange(len(sets)) ]
    
    for setnum, s in enumerate(sets):
        for chest in chests:
            if chest[0] in s:
                chestgroups[setnum].append(chest)
        for key in keys:
            if key in s:
                keygroups[setnum].append(key)


    subsols = []
    for subkeys, subchests in zip(keygroups, chestgroups):
        subsol = och(subchests, subkeys)
        if subsol is None:
            return "IMPOSSIBLE"
        subsols.append(subsol)

    # now merge the sub solutions:
    sol = []
    print "SUBSOLS"
    print subsols
    while any(subsols):
        subsols = filter(lambda l: len(l), subsols)
        first = min(subsols)
        sol.append(first.pop(0))

    return " ".join(str(s) for s in sol)


### PROCESS INPUT FILE ###

if __name__ == '__main__':

    f = open(sys.argv[1])
    fout = open(sys.argv[1].replace('.in','.out'),'w')

    T = int(f.readline())
    for case in xrange(T):
        K, N = [int(kn) for kn in f.readline().split()]
        keys = [int(ks) for ks in f.readline().split()]
    
        chests = [[int(ii) for ii in f.readline().split()] for _ in xrange(N)]
        ans = do(keys, chests)  
        print ans
        fout.write('Case #%d: %s\n'%(case+1,ans))

