#!/usr/bin/python

# Dan Seminara

import fileinput

# Ken's strategy should be: if he has a block heavier than hers, play the least one that is heavier
#  otherwise play his lightest block

# In order for Naomi not to reveal to Ken that she is lying, she has to either lie higher than
# any of Ken's blocks and have her block still be heavier than his lightest, lie higher to force
# Ken to play higher to remove one of Ken's high block from play

def war(ns,ks):
    nps = 0
    for n in ns:
        k_higher = [k for k in ks if k > n]
        if len(k_higher) > 0:
            k = min(k_higher)
        else:
            k = min(ks)
        ks.remove(k)
        if k < n:
            nps += 1
    return nps

def ken_strategy(n,ks):
    k_higher = [k for k in ks if k > n]
    if len(k_higher) > 0:
        return min(k_higher)
    else:
        return min(ks)

def deceitful_war(ns,ks):
    nps = 0
    ns.sort()
    ks.sort()
    for n in ns:
        i = 0
        while i < len(ks) and n > ks[i]:
            i += 1
        if i == 0:
            ks = ks[:-1]
        elif i == len(ks):
            nps += len(ks)
            break
        else:
            ks.remove(ks[i-1])
            nps +=1
    return nps

def main():
    inp = []
    for i,line in enumerate(fileinput.input()):
        if i == 0:
            continue
        inp.append(line.strip())
    games = zip(*[iter(inp)]*3)
    for i,game in enumerate(games):
        ns = [float(x) for x in game[1].split(' ')]
        ks = [float(x) for x in game[2].split(' ')]
        print('Case #%d: %d %d ' % (i+1,deceitful_war(ns.copy(),ks.copy()), war(ns.copy(),ks.copy())))

    

if __name__ == '__main__':
    main()