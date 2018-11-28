
import sys
import numpy as np
import pandas as pd
from collections import OrderedDict

class KeySet:
    def __init__(self):
        self.locker = [0 for i in xrange(200)]

    def add( self, keys ):
        for key in keys:
            self.locker[key] += 1

    def take(self,  key ):
        self.locker[key] -= 1
        return key

    def __getitem__(self, key):
        return self.locker[key]

    def has_key( self, key):
        return self.locker[key] > 0

    def __str__(self):
        keytypes_held = self.get_set()
        d = dict(map(lambda x: (x, self.locker[x]), keytypes_held))
        return str(d)

    def get_set(self):
        return filter(self.has_key, xrange(200))

class Chest:
    def __init__(self, keytype, keys):
        self.keytype = keytype
        self.keys = keys

    def __str__(self):
        return 'Lock %d : Keys %s' % (self.keytype, self.keys)

    def has_key(self, kt):
        return kt in self.keys

def remaining_locks(chests, keytype, status):
    predicated = filter(lambda x: chests[x].keytype == keytype and status[x] is LOCK, range(len(status)) )
    #print '    Remaining locks of type %d: %d' % (keytype, len(predicated))
    return len(predicated)

OPEN = 0
LOCK = 1

def get_next_chest(keyset, chests, status):
    for i in xrange(len(status)):
        kt = chests[i].keytype
        if status[i] is LOCK and keyset.has_key(kt):
            #print '    Considering %d' % (i +1)
            #print '      %s' % chests[i]
            if keyset[kt] > 1:
                #print 'More than one key of type %d' % kt
                return i
            if remaining_locks(chests, kt, status) == 1:
                #print 'Last lock of type %d' % kt
                return i
            if kt in chests[i].keys:
                #print 'Key %d retrievable from this chest' % kt
                return i
            reachable = reachable_keys(keyset, chests, status, removed_key=kt)
            if kt in reachable:
                #print 'Keytype %d still reachable later' % kt
                return i
    #print 'Couldn\'t find a candidate'
    return -1

def tree_search_one(keylist, chests, status):
    openable_chests = filter(lambda z: chests[z].keytype in keylist and status[z] is LOCK, range(len(status)))
    reachable = reduce(lambda x,y: x + chests[y].keys, openable_chests,[]  ) 
    return OrderedDict.fromkeys(reachable + keylist).keys()


def reachable_keys(keyset, chests, status, removed_key=None):
    keylist = keyset.get_set()
    if removed_key is not None:
        keylist.remove(removed_key)
    newkeylist = tree_search_one(keylist, chests, status)
    while (len(keylist) != len(newkeylist)):
        keylist = newkeylist
        newkeylist = tree_search_one(keylist, chests, status)
    #print '    Reachable keys: %s' % keylist
    return keylist


def process(start_keys, all_chests):
#    for i, c in zip(range(len(all_chests)), all_chests): print i+1, ' ', c
    ks = KeySet()
    ks.add(start_keys)
    #print 'Staring keys: %s' % ks
    status = [LOCK for i in xrange(len(all_chests))]

    steps = []
    while( any(status) ):
        nc = get_next_chest(ks, all_chests, status)
        #print '  Got %d' % (nc + 1)
        if nc == -1:
            return []
        steps += [nc]
        #print '  Steps so far: %s' % map(lambda x: x+1,steps)
        ks.take(all_chests[nc].keytype)
        ks.add(all_chests[nc].keys)
        #print '  Keyset: %s' % ks
        status[nc] = OPEN
    #print '  Status: %s' % status
    
    return steps

if __name__ == '__main__':
    infile = open(sys.argv[1], 'rb')
    lines = map(lambda x: x.rstrip(), infile.readlines())

    N_cases = int(lines[0])  # Number of cases
    lineIdx = 1
    caseNo = 1

    while (lineIdx < len(lines) and caseNo <= N_cases):
        K, N  = map(int, lines[lineIdx].rstrip().split(' '))
        #print 'K: %d, N: %d' % (K,N)
        lineIdx += 1
        start_keys = map(lambda x: int(x) - 1, lines[lineIdx].rstrip().split(' '))
        lineIdx += 1
        all_chests = [[] for x in range(N)]
        for chest in xrange(N):
            X = map(int, lines[lineIdx].rstrip().split(' '))
            keytype = X[0] - 1
            keys_inside = X[1]
            keys = map(lambda x: x-1, X[2:])
            all_chests[chest] = Chest(keytype, keys)
            lineIdx += 1
        caseAnswer = process(start_keys, all_chests)
        if len(caseAnswer) == 0:
            casestr = 'IMPOSSIBLE'
        else:
            casestr = ' '.join(map(lambda x: str(x+1), caseAnswer))
        print 'Case #%d: %s' % (caseNo, casestr)
        caseNo += 1
        

