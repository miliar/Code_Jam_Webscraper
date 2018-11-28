#/usr/bin/env python2.7
#-*- coding:utf-8 -*-
#huanghaiping2@gmail.com

import sys

def readline():
    return sys.stdin.readline()

def deceitful_war_score(naomi_blocks, ken_blocks):
    l_naomi_blocks = []
    l_naomi_blocks.extend(naomi_blocks)
    l_naomi_blocks.sort(reverse=True)
    l_ken_blocks = []
    l_ken_blocks.extend(ken_blocks)
    l_ken_blocks.sort(reverse=True)
    naomi_score = 0
    
    pairs = []
    for w in l_ken_blocks:
        if w > l_naomi_blocks[0]:
            pairs.append((l_naomi_blocks.pop(-1), w))
        else:
            pairs.append((l_naomi_blocks.pop(0), w))

    for n, k in pairs:
        if n > k:
            naomi_score += 1
    return naomi_score

def war_score(naomi_blocks, ken_blocks):
    l_ken_blocks = []
    l_ken_blocks.extend(ken_blocks)
    naomi_score = 0
    for w in naomi_blocks:
        kenWin = False
        for i,kw in enumerate(l_ken_blocks):
            if kw > w:
                l_ken_blocks.pop(i)
                kenWin = True
                break
        if not kenWin:
            naomi_score += 1
    return naomi_score
    

if __name__ == '__main__':
    T = int(readline())
    for i in xrange(T):
        print "Case #%s:" % (i+1),
        N = int(readline())
        naomi_blocks = [float(i) for i in readline().split(' ')]
        ken_blocks = [float(i) for i in readline().split(' ')]
        naomi_blocks.sort()
        ken_blocks.sort()
        print deceitful_war_score(naomi_blocks, ken_blocks),
        print war_score(naomi_blocks, ken_blocks)
