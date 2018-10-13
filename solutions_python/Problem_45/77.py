from __future__ import with_statement
import copy
import sys

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def count_bribe(pos, array):
    coins = 0
    array[pos] = 0
    #print array
    for i in range(pos + 1, len(array)):
        #print i,
        if array[i] == 0:
            break
        coins += 1
    #print
    for i in reversed(range(0, pos)):
        #print i,
        if array[i] == 0:
            break
        coins += 1
    #print
    #print "Pos result", coins
    return coins

def release_cost(positions, array):
    coins = 0
    for pos in positions:
        #print "Pos", pos
        coins += count_bribe(pos, array)
    #print "Perm result", coins
    return coins

def count_coins(data):
    array = [1 for x in range(data[0] + 2)]
    array[0] = 0
    array[-1] = 0
    result = []
    for perm in all_perms(data[2]):
        #print "Perm", perm
        result.append(release_cost(perm, copy.copy(array)))
    return min(result)


with open(sys.argv[1]) as f:
    lines = [l[:-1] for l in f.readlines()]
    cases = int(lines[0])
    data = {}
    for i,line in enumerate(lines[1::2]):
        data[i] = [int(x) for x in line.split(" ")]
    for i,line in enumerate(lines[2::2]):
        data[i].append([int(x) for x in line.split(" ")])
    
    for case in range(0, cases):
        print "Case #%i: %i" % (case + 1, count_coins(data[case]))
    

