import sys

file = open(sys.argv[1])
out = open('out.txt', 'w')

N = int(file.readline())

case = 1

def get_rep(pair):
	val = C_dict.get(pair, -1)
	if val == -1:
		val = C_dict.get(pair[::-1], -1)
	return val

def check_opp(pair):
#	print pair, D_set
	if pair in D_set or pair[::-1] in D_set:
#		print pair, 'success'
		return 1
	return 0

def reduce_final(final):
	if len(final) < 2:
		return final
	while len(final) > 1:
		pair = final[-2] + final[-1]
		val = get_rep(pair)
		if val != -1:
			final.pop(len(final)-1)
			final[-1] = val
		else:
			last = final[-1]
			for c in final[:-1]:
				if check_opp(c + last):
					final = []
					break
			break
	return final

for line in file:
	arr = line.split()
	C = int(arr[0])
	C_dict = {}
	i = 1
	while i <= C:
		key = arr[i][:2]
		val = arr[i][2]
		C_dict[key] = val
		C_dict[key[::-1]] = val
		i += 1
	D = int(arr[i])
	i += 1
	D_set = set()
	end = C + D + 2
	while i < end:
		val = arr[i]
		D_set.add(val)
		D_set.add(val[::-1])
		i += 1
	N = int(arr[i])
	i += 1
	seq = arr[i]
	i = 0
	final = []
	while i < N:
		final.append(seq[i])
#		print final
		final = reduce_final(final)
#		print 'reduced: ', final
		i += 1
	print case, seq, final
	res = 'Case #' + str(case) + ': ['
	for c in final:
		res += str(c) + ', '
	if len(final) > 0:
		res = res[:-2]
	out.write(res + ']\n')
	case += 1
