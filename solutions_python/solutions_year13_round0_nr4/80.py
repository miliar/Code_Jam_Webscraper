#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem D. Treasure
# https://code.google.com/codejam/contest/2270488/dashboard#s=p3
#

import sys
import itertools


class Chest:
    def __init__(self, no, key, inside):
        self.no = no
        self.key = key
        self.inside = inside


class Success(Exception):
    pass


def openchest(keymap, chests):
    for chest in chests:
        if chest.key not in reduce(lambda x,y: x+y, [c.inside for c in chests if c != chest],
                                   [key for key,count in keymap.items() if count]):
            return

    for cindex, chest in enumerate(chests):
        cnt = keymap.get(chest.key)
        if cnt:
            # open the chest
            newchests = chests[:cindex] + chests[cindex+1:]
            if not newchests:
                return (chest.no,)

            newkeymap = keymap.copy()
            newkeymap[chest.key] = cnt - 1
            for key in chest.inside:
                newkeymap[key] = newkeymap.get(key, 0) + 1

            result = openchest(newkeymap, newchests)
            if result:
                return (chest.no,) + result


def solve(keys, chests):
    for chest in chests:
        if chest.key not in reduce(lambda x,y: x+y, [c.inside for c in chests if c != chest], keys):
            return 'IMPOSSIBLE'

    allkeys = keys[:]
    for chest in chests:
        allkeys += chest.inside
    for chest in chests:
        if chest.key not in allkeys:
            return 'IMPOSSIBLE'
        allkeys.remove(chest.key)

    # keys list is slowly
    keymap = {}
    for key in keys:
        keymap[key] = keymap.get(key, 0) + 1

    result = openchest(keymap, tuple(chests))
    return ' '.join(str(n) for n in result) if result else 'IMPOSSIBLE'


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        K, N = map(int, IN.readline().split())
        keys = map(int, IN.readline().split())
        chests = []
        for n in range(N):
            tmp = map(int, IN.readline().split())
            chests.append(Chest(n + 1, tmp[0], tmp[2:]))
        #sys.stderr.write('Case #%d: %d chests\n' % (index + 1, len(chests)))
        OUT.write('Case #%d: %s\n' % (index + 1, solve(keys, chests)))


def makesample(Nmax=20, maxkeys=40, T=25):
    import random
    def makekeys():
        #return [random.randint(1, 200) for k in range(random.randint(1, maxkeys))]
        return [random.randint(1, maxkeys) for k in range(random.randint(1, maxkeys))]

    print T
    for index in range(T):
        keys = makekeys()
        chests = [Chest(n+1, random.randint(1, maxkeys), makekeys())
                  for n in range(random.randint(1, Nmax))]
        print len(keys), len(chests)
        print ' '.join(map(str, keys))
        for chest in chests:
            print chest.key, len(chest.inside), ' '.join(map(str, chest.inside))


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

