file = open("A-small-attempt1.in")
cn = file.readline()

#print int(cn)

def base10toN(num,n):
	new_num_string=''
	current=num
	while current!=0:
		remainder=current%n
		remainder_string=str(remainder)
		new_num_string=remainder_string+new_num_string
		current=current/n
	return new_num_string


def is_happy(num, base, s = False):
	st = base10toN(num, base)

	if not s:
		s = set([num])

	res = 0
	for i in st:
		res += int(i)**2
	
	hap = 0
	for i in base10toN(res, base):
		hap += int(i)
	
	if hap == 1:
		return True
	if res in s:
		return False

	s.add(res)
	return is_happy(res, base, s)


def treat_case(case_num):
	bases =  map(int, file.readline().strip('\n').split(' '))
	lowest = 1
	while lowest:
		lowest += 1
		good = True
		for i in bases:
			if not is_happy(lowest, i): 
				good = False
				break
		if good:
			break
	print "Case #%i: %i" % (case_num, lowest)

for case in range(int(cn)):
	treat_case(case+1)
