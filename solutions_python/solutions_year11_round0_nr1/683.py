import pprint

def read_file(file):
	f = open(file,'r')
	count = 0
	cases = []
	for line in f:
		count += 1
		if count == 1:
			n = int(line.strip())
		else:
			temp = line.strip().split()
			n = int(temp[0])
			btncount = 0
			case = {}
			case['O'] = []
			case['B'] = []
			for x in temp[1:]:
				if x in ('O','B'):
					bot = x
					btncount += 1
				else: 
					btn = int(x)
					case[bot].append({'count':btncount,'btn':btn})
			cases.append(case)
	return cases
			
def bot_strategy(case):
	ocount = 0
	bcount = 0
	opos = 1
	bpos = 1
	odone = False
	bdone = False
	seconds = 0
	
	if ocount >= len(case['O']):
		odone = True
	if bcount >= len(case['B']):
		bdone = True
			
	while(odone == False or bdone == False):
		if odone == True:
			next = 'B'
		elif bdone == True:
			next = 'O'
		elif case['O'][ocount]['count'] < case['B'][bcount]['count']:
			next = 'O'
		else: next = 'B'
		
		# O move
		if odone == False:
			if opos == case['O'][ocount]['btn'] and next == 'O':
				ocount += 1 # O pushes button
			elif opos < case['O'][ocount]['btn']:
				opos += 1 # O moves forward one button
			elif opos > case['O'][ocount]['btn']:
				opos -= 1 # O moves back one button
			else: pass # O waiting on B
		
		# B move
		if bdone == False:
			if bpos == case['B'][bcount]['btn'] and next == 'B':
				bcount += 1 # B pushes button
			elif bpos < case['B'][bcount]['btn']:
				bpos += 1 # B moves forward one button
			elif bpos > case['B'][bcount]['btn']:
				bpos -= 1 # B moves back one button
			else: pass # B waiting on O
		
		seconds += 1
		
		if ocount >= len(case['O']):
			odone = True
		if bcount >= len(case['B']):
			bdone = True
		
		output = "O: %d %s, B: %d %s, %d secs" % (opos,odone,bpos,bdone,seconds)
		
		print output
		
	return seconds
		
#pp = pprint.PrettyPrinter(indent=4)

cases = read_file('A-large.in')
#print pp.pprint(cases)

for index,case in enumerate(cases):
	seconds = bot_strategy(case)
	output = "Case #%d: %d" % (index+1,seconds)
	f = open('bot_trust.out','a')
	print >>f, output
	f.close()



			