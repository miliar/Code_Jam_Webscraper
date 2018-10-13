import sys

def process(s, case):
	substitute = {}
	s = s.split()
	index = 1
	for item in [s[i+1] for i in range(int(s[0]))]:
		substitute[item[:2]] = item[2:]
		substitute[item[:2][::-1]] = item[2:]
		index += 1
	
	
	replacement = {}
	for item in [s[index+j+1] for j in range(int(s[index]))]:
		replacement[item[0]] = item[1]
		replacement[item[1]] = item[0]
	
	
	input = s[-1]
	result = '-'
	for c in input:
		if result[-1]+c in substitute.keys():
			result = result[:-1]+ substitute[result[-1]+c]
		elif c in replacement.keys() and replacement[c] in result:
			result = '-'
		else:
			result += c
	
	
	result = result[1:]
	output = 'Case #' + str(case) + ': [' + ', '.join(result) + ']'
	
	return output



filename = sys.argv[1]
f = open(filename, 'r')
inputs = f.readlines()
case = 1
outputs = []
for i in inputs[1:]:
	outputs.append(process(i,case)+'\n')
	case += 1


fo = open(filename.split('.')[0]+'.out','w+')
fo.writelines(outputs)
fo.close()
f.close()