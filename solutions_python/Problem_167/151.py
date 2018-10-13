import math
import os
import itertools


def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result

def sums(subsets):
    res = []
    for l in subsets:
        _sum = sum(l)
        if _sum not in res:
            res.append(_sum)            
    return sorted(res)

for f in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if f.endswith(".in"):
        f_in = open(f)
        f_out = open(f[:-3] + '.out', 'w')

lines = f_in.read().split('\n')
t1 = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), lines[1::2]))
t2 = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), lines[2::2]))
tests = list(zip(t1, t2))
d_out = []

for num_test, test in enumerate(tests, 1):
    C = test[0][0]
    V = test[0][2]
    denom = test[1]
    res = 0
    subs = subsets(denom)
    _sums = sums(subs)
    for i in range(V+1):
        if i not in _sums:
            denom.append(i)
            subs = subsets(denom)
            _sums = sums(subs)
            res += 1
    d_out.append('Case #' + str(num_test) + ': ' + str(res) + '\n')


f_out.writelines(d_out)
f_out.close()
f_in.close()
