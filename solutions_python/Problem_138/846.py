__author__ = 'rcarino'
import sys
from pprint import pprint

def reg_war(n_l, k_l):
    wins = 0
    while n_l:
        n_v = n_l.pop(0)
        for i in range(len(k_l)):
            if k_l[i] > n_v:
                k_l.pop(i)
                break
        # Naomi wins
        if len(k_l) > len(n_l):
            k_l.pop(0)
            wins += 1
    return wins

def deceit_war(n_l, k_l):
    wins = 0
    while n_l:
        n_v = n_l.pop(0)
        # can't beat anything
        if n_v < k_l[0]:
            k_l.pop()
        else:
            k_l.pop(0)
            wins += 1
    return wins

with open(sys.argv[1]) as f:
# with open('easy_war') as f:
    contents = f.readlines()
    for i in range(int(contents.pop(0))):
        contents.pop(0)
        n_l = sorted([float(f) for f in contents.pop(0).split(' ')])
        k_l = sorted([float(f) for f in contents.pop(0).split(' ')])
        print 'Case #{0}: {1} {2}'.format(i+1, deceit_war(list(n_l), list(k_l)), reg_war(list(n_l), list(k_l)))