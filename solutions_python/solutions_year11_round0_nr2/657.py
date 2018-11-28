import sys

def process(s, case):
	sub = {}
	s = s.split()
	index = 1
	for i in range(int(s[0])):
		item = s[i+1]
		sub[item[:2]] = item[2:]
		sub[item[:2][::-1]] = item[2:]
		index += 1
	
	
	rep = {}
	for j in range(int(s[index])):
		item = s[index+j+1]
		rep[item[0]] = item[1]
		rep[item[1]] = item[0]
	
	
	input = s[-1]
	result = '-'
	for c in input:
		if result[-1]+c in sub.keys():
			result = result[:-1]+ sub[result[-1]+c]
		elif c in rep.keys() and rep[c] in result:
			result = '-'
		else:
			result += c
	
	
	result = result[1:]
	output = 'Case #' + str(case) + ': ['
	for c in result:
		output += c + ', '
	
	if len(result) > 0:
		return output[:-2] + ']'
	else:
		return output + ']'




filename = sys.argv[1]
f = open(filename, 'r')
inputs = f.readlines()
case = 1
outputs = []
for i in inputs[1:]:
	outputs.append(process(i,case)+'\n')
	case += 1


fo = open('m_out.txt','w+')
fo.writelines(outputs)
fo.close()
f.close()	