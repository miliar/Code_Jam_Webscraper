import sys

def process(s,count):
	input = s.split()[1:]
	totalTime = 0
	currentVal = {'O':1,'B':1}
	currentTime = 0
	prevColor = ''
	for i in range(0,len(input),2):
		time_needed = abs(int(input[i+1]) - currentVal[input[i]])
		if prevColor == input[i]:
			td = time_needed + 1
			totalTime += td
			currentTime += td
		else:
			if time_needed <= currentTime:
				currentTime = 1
				totalTime += 1
			else:
				currentTime = time_needed - currentTime  + 1
				totalTime += currentTime
		currentVal[input[i]] = int(input[i+1])
		prevColor = input[i]
	
	return 'Case #' + str(case) + ': ' + str(totalTime)


filename = sys.argv[1]
f = open(filename, 'r')
inputs = f.readlines()
case = 1
outputs = []
for i in inputs[1:]:
	outputs.append(process(i,case)+'\n')
	case += 1


fo = open('a_out.txt','w+')
fo.writelines(outputs)
fo.close()
f.close()	