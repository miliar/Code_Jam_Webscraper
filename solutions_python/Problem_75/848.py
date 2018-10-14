def calc(case): 
	parts = case.split()
	
	partc = 0

	#Combinations
	if int(parts[partc]) > 0:
		combos = combineds(parts, partc + 1, int(parts[partc]))
		partc = partc + int(parts[partc]) + 1
	else:
		combos = {}
		partc = partc + 1

	#Oppositions
	if int(parts[partc]) > 0:
		opps = opposeds(parts, partc + 1, int(parts[partc]))
		partc = partc + int(parts[partc]) + 1
	else:
		opps = set()
		partc = partc + 1

	#invoking
	if int(parts[partc]) > 0:
		result = invoke(parts[partc + 1], combos, opps)
	else:
		result = []

	return toString(result)
	

def toString(result):
	data = ', '.join(result)
	return '[' + data + ']'


def opposeds(parts, start, length):
	opps = []
	for opp in parts[start:start+length]:
		opps.append((opp[0], opp[1]))

	return set(opps)


def combineds(parts, start, length):
	combos = {}
	for combo in parts[start:start+length]:
		combos[(combo[0], combo[1])] = combo[2]

	return combos
	

def invoke(elements, combos, opps):
	magick = []

	magick.append(elements[0])

	for e in elements[1:]:
		if len(magick) == 0:
			magick.append(e)
		elif (e, magick[-1]) in combos:
			magick = magick[:-1] + [combos[(e, magick[-1])]]
		elif (magick[-1], e) in combos:
			magick = magick[:-1] + [combos[(magick[-1], e)]]
		else:
			for m in set(magick):
				if (m, e) in opps or (e, m) in opps:
					magick = []
					break
			else:
				magick.append(e)

	return magick

f = open('B-large.in', 'r')
lines = f.readlines()   
f.close()
c = lines[0].split()[0]
#print c     
cases = [r.strip() for r in lines[1:]]
#print cases  
                       
of = open('output_b_large.txt', 'w')

for idx, case in enumerate(cases):
	of.write('Case #%(idx)i: %(i)s\n' % {'idx': idx + 1, 'i': calc(case)})                          
   
of.close()
