file = open("A-small-attempt0.in")
cn = file.readline()

#print int(cn)

def tobase(num, base):
	if num == '':
		return 0
	if len(num) == 1:
		try:
			return int(num)
		except:
			return ord(num)  - ord('a') + 1
	ch = num[-1]
	try: 
		cch = int(ch)
	except:
		cch = ord(ch)  - ord('a') + 1
	print ch, cch, num[:-1]
	return cch + tobase(num[:-1], base)*base


def treat_case(case_num):
	ma =  file.readline().strip('\n')
	
	di = dict()
	ne = ''
	maxim = 1
	for i in ma:
		if i in di:
			ne += str(di[i])
		else:
			if len(di) == 1:
				di[i] = 0
			else:
				di[i] = maxim
				maxim += 1
			ne += str(di[i])
	
	ba = max(ne)
	try:
		bas = int(ba) + 1
	except:
		bas = ord(ba)  - ord('a') + 11
	
	print "Case #%i: %i" % (case_num, int(ne, bas))

for case in range(int(cn)):
#	case_arg = map(int, file.readline().strip('\n').split(' '))
	treat_case(case+1)
