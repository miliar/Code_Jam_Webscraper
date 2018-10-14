import sys

def flip(pancake_state, idx, num):
    for i in xrange(num):
        if pancake_state[idx+i] == '+':
            ps_l[idx+i] = '-'
        else:
            ps_l[idx+i] = '+'
    return pancake_state;

lines = open(sys.argv[1], "r").read().splitlines()
res = ""

cases = int(lines[0])
idx = 1

for c in xrange(cases):
    (pancake_state, flip_sim) = lines[c+1].split(' ')
    flip_sim = int(flip_sim)
    ps_l = list(pancake_state)
    flips = 0
    flag = True
    for i in xrange(len(ps_l) - flip_sim + 1):
        if ps_l[i] == '-':
            flips += 1
            ps_l = flip(ps_l, i, flip_sim)
    for i in xrange(flip_sim - 1):
        if ps_l[-(i+1)] == '-':
            flag = False
    if flag:
        res += "Case #%d: %d\n" %(c+1, flips)
    else:
        res += "Case #%d: IMPOSSIBLE\n" %(c+1)
open(sys.argv[2], "w").write(res)


