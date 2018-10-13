file = open("C-small-attempt0.in")
cn = file.readline()

def neigh(l, pos, dir):
	if len(l) <= 1:
		return 0
	res = 0
	jump = 1
	if dir:
		while pos + jump < len(l):
			if l[pos + jump]:
				res += 1
			else:
				break
			jump += 1
	else:
		while pos - jump >= 0:
			if l[pos - jump]:
				res += 1
			else:
				break
			jump += 1
	return res



def all_perms_num(str, n):
	if len(str) <=n:
		yield str
	else:
		for i in range(len(str)):
			for perm in all_perms_num(str[:i]+str[i+1:], n):
				yield  [str[i]] + perm

def treat_case(case_num, args):
	rel =  map(int, file.readline().strip('\n').split(' '))
	coins = 99999
	for cas in all_perms_num(rel, 0):
		c = 0
		cells = [0] + [1] * args[0]
		#print '---'
		for i in cas:
			c += neigh(cells, i, 0) + neigh(cells, i, 1)
		#	print cells, neigh(cells, i, 0) + neigh(cells, i, 1), i
			cells[i] = 0
		if c < coins:
			coins = c


	print "Case #%i: %i" % (case_num, coins)

for case in range(int(cn)):
	case_arg = map(int, file.readline().strip('\n').split(' '))
	treat_case(case+1,case_arg)
