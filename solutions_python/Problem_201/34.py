
# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()
    

def solve(n, k):
    #debug(str(ps))
    #debug(str(k))

    space = n-1
    rest = k-1

    if rest == 0:
        return str(space/2 + space % 2) + " " + str(space/2)

    if space % 2 == 0:
        next_n = space / 2 + space % 2
        next_k = rest / 2 + rest % 2
    elif rest % 2 == 0:
        next_n = space / 2
        next_k = rest / 2 + rest % 2
    else:
        next_n = space / 2 + space % 2
        next_k = rest / 2 + rest % 2

    return solve(next_n, next_k)

#input_file = "sample.in"
#input_file = "C-small-2-attempt0.in"
input_file = "C-large.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"), 'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip().split()
    ans = solve(long(l[0]), long(l[1]))
    print("Case #" + str(tc+1) + ": " + ans)

