def handle(testcase):
	testcase = [int(elem) for elem in testcase.split()]
	N = testcase[0]
	S = testcase[1]
	p = testcase[2]
	t = testcase[3:]
	count3n1 = len([elem for elem in t if elem%3 == 1 and (elem/3)+1 >= p])
	vec3n1c = [elem for elem in t if elem%3 != 1]
	count3n1c = 0
	surprised = 0
	for elem in vec3n1c:
		if elem%3 == 0:
			if elem == 0:
				if p == 0:
					count3n1c += 1
			elif elem/3 >= p:
				count3n1c += 1
			elif (elem/3)+1 >= p and surprised < S:
				count3n1c += 1
				surprised += 1
		else:
			if (elem/3)+1 >= p:
				count3n1c += 1
			elif (elem/3)+2 >= p and surprised < S:
				count3n1c += 1
				surprised += 1
	return count3n1+count3n1c

f = open('sample.txt', 'r')
fout = open('output.txt', 'w')
fContent = f.read().split('\n')
T = int(fContent[0])
for i in range(T):
	fout.write('Case #'+ str(i+1) + ': ' + str(handle(fContent[i+1])) + '\n')
f.close()
fout.close()