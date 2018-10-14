import sys
import functools
import itertools

def group(iterable, n):
	iters = []
	for i in range(n):
		iters.append(itertools.islice(iterable, i, None, n))
	
	return zip(*iters)

input_data = list(line[:-1] for line in sys.stdin)[1:]

case = 1
for n_str, candy_str in group(input_data, 2):
	n = int(n_str)
	candy = sorted(int(x) for x in candy_str.split())
	xor_sum = lambda l: functools.reduce(lambda a, b: a ^ b, l, 0)
	if xor_sum(candy) == 0:
		result = str(sum(candy[1:]))
	else:
		result = "NO"
	
	print("Case #{}: {}".format(case, result))

	case+=1
