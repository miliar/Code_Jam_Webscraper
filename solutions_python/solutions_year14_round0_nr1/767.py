def magicTrick():
	for i in range(input()):
		NUMBER1 = input()
		ARRANGEMENT1 = []
		for j in range(4):
			temp = [int(p) for p in raw_input().strip().split()]
			ARRANGEMENT1.append(temp)
		NUMBER2 = input()
		ARRANGEMENT2 = []
		for j in range(4):
			temp = [int(p) for p in raw_input().strip().split()]
			ARRANGEMENT2.append(temp)
		SET1 = ARRANGEMENT1[NUMBER1 - 1]
		SET2 = ARRANGEMENT2[NUMBER2 - 1]
		C = 0
		VAL = 0
		for j in SET1:
			if j in SET2:
				VAL = j
				C += 1
		if C == 0:
			print 'Case #%d: '%(i+1), 'Volunteer cheated!' 
		elif C == 1:
			print 'Case #%d: '%(i+1), VAL 
		else:
			print 'Case #%d: '%(i+1), 'Bad magician!' 

if __name__ == '__main__':
	magicTrick()
		
