import collections
import math

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]


f = [i for i in open('B-large.in')]
f[-1] +='\n'
data = [i[:-1] for i in f]
cases = []
for i in range(int(data[0])):
	eaters = [int(i) for i in data[(i+1)*2].split(' ')]
	minimum = max(eaters)
	for j in range(1, max(eaters)):
		curr = j
		for eat in eaters:
			if eat > j:
				curr += math.ceil(eat/j)-1
		if curr < minimum:
			minimum = curr
	cases.append('Case #'+str(i+1)+': '+str(minimum))
f1 = open('output.txt','w')
[f1.write(i+'\n') for i in cases]