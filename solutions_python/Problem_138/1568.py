outwr = ''
waf = open('war.txt', 'r')
conts = waf.read().split('\n')
waf.close()

def prune(first, second, other = False):
	first = sorted(first)
	second = sorted(second)
	pointsA = len(first)
	pointsB = 0

	print('')
	for i in first:
		if second[-1] > i:
			j = 0
			while second[j] <= i:
				j += 1
			pointsA -= 1
			pointsB += 1
			del second[j]
		else:
			del second[-1]
		
	if other == False: return pointsA
	else: return pointsB

cases = int(conts[0])
pos = 1
for cn in range(cases):
	naomi = [float(i) for i in conts[pos+1].split(' ')]
	ken = [float(i) for i in conts[pos+2].split(' ')]
	
	pos += 3
	outwr += 'Case #' + str(cn+1) + ': ' + str(prune(ken, naomi, True)) + ' ' + str(prune(naomi, ken)) + '\n'
	
outf = open('outD.txt', 'w')
outf.write(outwr)
outf.close()