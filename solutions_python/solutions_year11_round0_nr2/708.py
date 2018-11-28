import pprint

def read_file(file):
	f = open(file,'r')
	count = 0
	cases = []
	for line in f:
		count += 1
		if count == 1:
			t = int(line.strip())
		else:
			case = {}
			case['combine'] = []
			case['oppose'] = []
			temp = line.strip().split()
			n = int(temp[0])
			if n == 0:
				next = 1
			else:
				next = n + 1
				for x in temp[1:next]:
					base = x
					case['combine'].append({'base1':base[0],'base2':base[1],'nonbase':base[2]})
			d = int(temp[next])
			if d == 0:	
				next_2 = next + 1
			else:
				next_2 = next + d + 1
				for x in temp[next+1:next_2]:
					opp = x
					case['oppose'].append({opp[0]:1,opp[1]:1})
			#n = int(temp[next_2])
			case['series'] = temp[next_2+1]
			cases.append(case)
	return cases
			
def invoke(case):
	series = []
	for c in case['series']:
		#print c
		if series == []:
			series.append(c)
		else:
			next = False
			for comb in case['combine']:
				if series[-1] == comb['base1'] and c == comb['base2']:
					series[-1] = comb['nonbase']
					next = True
					#print pp.pprint(series)
					break
				elif series[-1] == comb['base2'] and c == comb['base1']:
					series[-1] = comb['nonbase']
					next = True
					#print pp.pprint(series)
					break
			if next == True: continue
			for opp in case['oppose']:
				if c in opp:
					for char in series:
						if char != c and char in opp:
							series = []
							next = True
							#print pp.pprint(series)
							break
			if next == True: continue
			series.append(c)
			#print pp.pprint(series)
	return series
	
def series_to_string(series):
	string = '['
	count = 0
	for x in series:
		if count == 0:
			string += x
		else: string += ', ' + x
		count += 1
	string += ']'
	return string
		
pp = pprint.PrettyPrinter(indent=4)

cases = read_file('B-large.in')

#print pp.pprint(cases)

for index,case in enumerate(cases):
	series = invoke(case)
	string = series_to_string(series)
	output = "Case #%d: %s" % (index+1,string)
	f = open('magicka.out','a')
	print >>f, output
	f.close()



			