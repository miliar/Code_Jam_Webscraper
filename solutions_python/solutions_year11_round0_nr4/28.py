def main():
	fin = open('D-large.in','r')
	fout = open('output1.txt','w')
	
	T = int(fin.readline())
	
	for i in range(T):
		fin.readline()
		unsorted = map(int,fin.readline().strip().split(' '))
		reference = unsorted[:]
		reference.sort()
		
		sameCounter = 0
		
		for j in range(len(unsorted)):
			if unsorted[j] == reference[j]:
				sameCounter += 1
		
		print 'Case #' + str(i+1) + ': ' + str(len(unsorted) - sameCounter)
		fout.write('Case #' + str(i+1) + ': ' + str(len(unsorted) - sameCounter) + '\n')	

if __name__ == '__main__':
	main()
