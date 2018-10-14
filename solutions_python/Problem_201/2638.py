from math import floor, ceil

def find_min_stall(stalls, people):
	exps = []
	n = 0
	while sum(exps) < people:
		exps.append(2**n)
		n+=1
	exp = sum(exps)
	working_n = stalls - exp
	key_n = exps[-1]
	over = people - key_n
	rem = working_n % key_n
	div = working_n / key_n
	fact = (stalls / key_n) - 1
	line = [fact] * rem
	test = working_n - sum(line)
	needed = key_n - len(line)
	for i in range(needed):
		line.append(test / needed)
	sol = float(line[over])
	_max = int(ceil(sol/2))
	_min = int(floor(sol/2))
	return '{} {}'.format(_max, _min)

inp = open('/Users/aspittel/Downloads/C-small-2-attempt0.in')
inp = inp.read()

inp = inp.split('\n')

inp.pop(0)
inp.pop()

write_file = open('code_jam_med.txt', 'w+')
for idx, n in enumerate(inp):
	n = n.split(' ')
	write_file.write("Case #{}: {}\n".format(idx + 1, find_min_stall(int(n[0]), int(n[1]))))
