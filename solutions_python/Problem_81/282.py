import pprint, sys

def read_file(file):
	f = open(file,'r')
	count = 0
	cases = []
	line = f.readline()
	num = int(f.readline().strip())
	count = 0
	case = []
	for line in f:
		count += 1
		if count > num:
			cases.append({'string':case})
			num = int(line.strip())
			count = 0
			case = []
		else:
			case.append(line.strip())
	cases.append({'string':case})
	return cases
			
def calc_rpi(case):
	case['games'] = []
	case['wp'] = []
	case['owp'] = []
	case['oowp'] = []
	case['rpi'] = []
	for t in case['string']:
		win = 0
		loss = 0
		for s in t:
			if s == '1':
				win += 1
			elif s == '0':
				loss += 1
		case['wp'].append(float(win) / float(win+loss))
		case['games'].append(win+loss)
	for t in case['string']:
		owp = 0
		owpc = 0
		for index,item in enumerate(t):
			slen = case['games'][index]
			wp = case['wp'][index]
			if item == '1':
				wp *= slen 
				wp /= float(slen-1)
			elif item == '0':
				wp *= slen
				wp -= 1
				wp /= float(slen-1)
			else: continue
			owp += wp
			owpc += 1
		owp /= float(owpc)
		case['owp'].append(owp)
	for tindex,t in enumerate(case['string']):
		oowp = 0
		oowpc = 0
		for index,item in enumerate(t):
			if item != '.':
				oowp += case['owp'][index]
				oowpc += 1
		oowp /= float(oowpc)
		case['oowp'].append(oowp)
		case['rpi'].append(.25*case['wp'][tindex] + .5*case['owp'][tindex] + .25 * case['oowp'][tindex])
	return case
				
		
pp = pprint.PrettyPrinter(indent=4)

cases = read_file('A-large.in')

f = open('rpi.out','a')
for index,case in enumerate(cases):
	case = calc_rpi(case)
	output = "Case #%d: " % (index+1)
	print >>f, output
	for t in case['rpi']:
		print >>f, t
f.close()



			