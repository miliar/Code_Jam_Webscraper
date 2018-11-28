#!/usr/bin/env python

def extractrow(raw, match):
	rawsize = len(raw)
	res = []
	for c in range(rawsize):
		if(raw[c] == match or raw[c] == 'T'):
			res.append(c)
	return res

def extractset(raw, match):
	rawsize = len(raw)
	res = []
	for c in range(rawsize):
		row = extractrow(raw[c], match)
		for r in range(len(row)):
			res.append(row[r] + (c * rawsize))
	return res


		
def checkdraw(raw):
	for row in raw:
		# print raw[row]
		for c in raw[row]:
			if(c == '.'):
				return False
	return True


def readCard(f):
	card = {}
	card[0] = list(f.readline().rstrip().split(' '));
	card[1] = list(f.readline().rstrip().split(' '));
	card[2] = list(f.readline().rstrip().split(' '));
	card[3] = f.readline().rstrip().split(' ');
	return card

# main

f = open('data/A-small-attempt0.in', 'r')

cases = int(f.readline())

raw = []

for case in range(cases):
	case = {}
	case['ans1'] = f.readline().rstrip()
	case['card1'] = readCard(f)
	case['ans2'] = f.readline().rstrip()
	case['card2'] = readCard(f)
	
	raw.append(case)
	
# 	print match
# 	print len(match)
# 	
# 	print ans1
# 	print card1
# 	print ans2
# 	print card2
# 	
# 	print select1
# 	print select2
	
f.close()

f = open('data/A-small.out', 'w')
for casepos in range(cases):
	case = raw[casepos]
	ans1 = case['ans1']
	card1 = case['card1']
	ans2 = case['ans2']
	card2 = case['card2']
	
	select1 = card1[int(ans1) - 1]
	select2 = card2[int(ans2) - 1]
	
	match = set(select1) & set(select2)
	
	matchlen = len(match)
	
	s = "Case #" + str(casepos + 1)+ ": "
	
	if matchlen == 0:
		s += "Volunteer cheated!"
	elif matchlen == 1:
		s += next(iter(match))
	else:
		s += "Bad magician!"
		
	print s
	f.write(s + '\n')
	
f.close()




