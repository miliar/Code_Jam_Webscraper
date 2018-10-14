
def main():
	fin = open('A-large.in','r')
	fout = open('output.txt','w')
	
	T = int(fin.readline())
	
	for i in range(T):
		data = fin.readline().strip().split(' ')
		seq = []
		oSeq = []
		bSeq = []
		
		for j in range(1,len(data)-1,2):
			seq.append((data[j],int(data[j+1])))
			if data[j] == 'O':
				oSeq.append(int(data[j+1]))
			else:
				bSeq.append(int(data[j+1]))
		
		count = 0
		oPos = 1
		bPos = 1
		oIndex = 0
		bIndex = 0
		
		for step in seq:
			movesToPush = 0
			if step[0] == 'O':
				oIndex += 1
				movesToPush = abs(step[1]-oPos) + 1
				oPos = step[1]
				if bIndex < len(bSeq):
					if bSeq[bIndex] > bPos:
						bPos += min(bSeq[bIndex] - bPos, movesToPush)
					elif bSeq[bIndex] < bPos:
						bPos -= min(bPos - bSeq[bIndex], movesToPush)
			else:
				bIndex += 1
				movesToPush = abs(step[1]-bPos) + 1
				bPos = step[1]
				if oIndex < len(oSeq):
					if oSeq[oIndex] > oPos:
						oPos += min(oSeq[oIndex] - oPos, movesToPush)
					elif oSeq[oIndex] < oPos:
						oPos -= min(oPos - oSeq[oIndex], movesToPush)
			count += movesToPush
		
		print 'Case #' + str(i+1) + ': ' + str(count)
		fout.write('Case #' + str(i+1) + ': ' + str(count) + '\n')
		

if __name__ == '__main__':
	main()
