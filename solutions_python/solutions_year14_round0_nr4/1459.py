# https://code.google.com/codejam/contest/2974486/dashboard#s=p3
import sys

def readline():
    return sys.stdin.readline().rstrip()

def wins(first, second):
    win_f=0
    win_s=0
    for chosen_f in first:
        if any(k > chosen_f for k in second):
            second.remove(min(k for k in second if k > chosen_f))
            win_s+=1
        else:
            second.pop(0)
            win_f+=1
    return win_f


t = int(readline())
for case in range(t):
    n = int(readline())
    line = readline()
    naomi = [float(s) for s in line.split()]
    naomi.sort()
    line = readline()
    ken = [float(s) for s in line.split()]
    ken.sort()
    war_wins = wins(list(naomi), list(ken))
    deceipt_wins = n - wins(list(ken), list(naomi))
    print 'Case #{}: {} {}'.format(case+1, deceipt_wins, war_wins)


