import sys


def process(s,case):
	input = [int(i) for i in s.split()]
	if reduce(xor, input) == 0:
		output = str(sum(input)-min(input))
	else:
		output = 'NO'
	
	output = 'Case #' + str(case) + ': ' + output
	return output

def xor(a,b):
	return a^b



filename = sys.argv[1]
f = open(filename, 'r')
inputs = f.readlines()
case = 1
outputs = []
for i in range(2,len(inputs),2):
	outputs.append(process(inputs[i],case)+'\n')
	case += 1


fo = open('c_out.txt','w+')
fo.writelines(outputs)
fo.close()
f.close()	