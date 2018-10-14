import sys
data = open('p2-l.txt', 'r')
N = int(data.readline().strip('\n'))
output = open('p2-l_output.txt', 'w')

for i in range(N):
	T = data.readline().strip('\n')
	length = len(T)
	position = 0
	last = ""
	for k in range(length):
		if T[k] > last:
			position = k
			value = T[:k] + str(int(T[k])*(10**(length-k-1)) - 1)
		elif T[k] < last:
			break
		if k == length-1:
			value = T
		last = T[k]
	output.write('Case #' + str(i+1) + ': ' + value + '\n')