if __name__ == "__main__":
	with open("B-small-attempt0.in", 'r') as inputf:
		outputf=open("B_out.out",'w')
		line=inputf.readline()
		line=line.rstrip('\n')
		test_num=int(line)
		
		for test in range(test_num):
			line = inputf.readline()
			line = line.rstrip('\n')
			info = line.split(' ')
			numbers = []

			a = int(info[0])
			b = int(info[1])
			k = int(info[2])

			for i in range(a):
				for j in range(b):
					numbers.append((i)&(j))

			numbers.sort(reverse=True)

			for i in range(k):
				l = k - i -1
				if l in numbers:
					break

			num = len(numbers)-numbers.index(l)

			result = "Case #%d: %d" % (test+1, num)
			outputf.write(result)

			if test!=test_num-1:
				outputf.write('\n')




			

