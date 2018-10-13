import math
import os

for f in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if f.endswith(".in"):
        f_in = open(f)
        f_out = open(f[:-3] + '.out', 'w')

lines = f_in.read().split('\n')
tests = map(lambda x: map(lambda y: int(y), x.split(' ')), lines[2::2])
d_out = []

for num_test, test in enumerate(tests, 1):
	diffs = map(lambda x,y:  x-y, test[:-1:], test[1:])
	diffs = [x for x in diffs if x > 0]
	method1 = sum(diffs)
	max_diff = max(diffs) if len(diffs) else 0
	method2 = sum([min(max_diff, x) for x in test][:-1])
	d_out.append('Case #' + str(num_test) + ': ' + str(method1) + ' ' + str(method2) + '\n')
 

f_out.writelines(d_out)
f_out.close()
f_in.close()