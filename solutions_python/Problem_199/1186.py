# Leon Xueliang Liu 2017

with open('A-large.in', 'r') as f:
	content = f.readlines()

T = int(content[0]) # # of cases
data = [[val for val in line.split()] for line in content[1:]]

result = [] # list of results

def numerize(string):
	s = []
	for i in range(len(string)):
		if string[i] == '+':
			s.append(True)
		else:
			s.append(False)
	return s

for n in range(T):
	string = numerize(data[n][0])
	K = int(data[n][1])
	L = len(string)
	f = 0

	for i in range((L-K) // 2+1):
		if not string[i]:
			for j in range(K):
				string[i+j] = not string[i+j]
			f += 1
		if not string[L-1-i]:
			for j in range(K):
				string[L-1-i-j] = not string[L-1-i-j]
			f += 1
	f = str(f)
	for i in range(L):
		if not string[i]:
			f = 'IMPOSSIBLE'
			break
	result.append(f)		

#write to output
with open('A-large.txt','w+') as f:
	for count, flips in enumerate(result):
		f.write("Case #{}: {}\n".format(count+1, flips))

