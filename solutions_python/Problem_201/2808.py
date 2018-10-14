import sys
data = open('p3.txt', 'r')
N = int(data.readline().strip('\n'))
output = open('p3_output.txt', 'w')

class stall:
	occupied = False
	L = 0
	R = 0
	minimum = 0
	maximum = 0
	def calculate(self):
		self.minimum = min(self.L,self.R)
		self.maximum = max(self.L,self.R)
	def __init__(self, pos):
		self.position = pos

for i in range(N):
	T = data.readline().strip('\n').split()
	N = int(T[0])
	K = int(T[1])
	stalls = []
	for index in range(N+2):
		stalls.append(stall(index))
	stalls[0].occupied = True
	stalls[0].L = -1
	stalls[-1].occupied = True
	stalls[-1].R = -1
	for j in range(K):
		for index in range(1,N+1):
			if not stalls[index].occupied:
				stalls[index].L = stalls[index-1].L+1
			else:
				stalls[index].L = -1
		for index in range(N-1, 0, -1):
			if not stalls[index].occupied:
				stalls[index].R = stalls[index+1].R+1
			else:
				stalls[index].R = -1
		for j in range(1, len(stalls)-1):
			stalls[j].calculate()
		temporary = sorted(stalls, key=lambda elem: (elem.minimum, elem.maximum), reverse=True)
		choice = temporary[0]
		stalls[choice.position].occupied = True
		
	output.write('Case #' + str(i+1) + ': ' + str(choice.maximum) + ' ' + str(choice.minimum) + '\n')


