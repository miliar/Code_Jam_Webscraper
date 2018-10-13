file = open("B-small-attempt1.in")
cn = file.readline()

#print int(cn)

def all_perms_num(str, n):
	if len(str) <=n:
		yield str
	else:
		for i in range(len(str)):
			for perm in all_perms_num(str[:i]+str[i+1:], n):
				yield  [str[i]] + perm

def treat_case(case_num):
#	print file.readline()
	ma =  int(file.readline().strip('\n'))
	ma *= 10
	l = []
	for i in all_perms_num(list(str(ma)), 0):
		res = int(reduce(lambda a,b: a+b, i))
		l += [res]
	l = list(set(l))
	l.sort()
	print "Case #%i: %i" % (case_num, l[l.index(ma/10)+1])

for case in range(int(cn)):
#	case_arg = map(int, file.readline().strip('\n').split(' '))
	treat_case(case+1)
