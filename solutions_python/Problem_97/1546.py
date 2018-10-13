#10 to 40
#10 <= n < m <= 40
input = open("C:\\Users\\David\\Downloads\\C-small-attempt1.in").readlines()

def shift(a):
	return a[-1] + a[0:-1]

def recycle(A, B):
	count = 0
	# A, B+1
	for i in range(A, B+1): # 1111..2222
		for j in range(i+1, B+1): # 1111: 1112..2222
			number = str(j)
			for k in range(0, len(number)):
				number = shift(number)
				if str(i) == number:
					#print i, j, i+j
					count+=1
					break
	return count
#print recycle(1111,2222)
count = 1
for line in input[1:]:
	tokens = line.split()
	print "Case #" + str(count) + ": " + str(recycle(int(tokens[0]), int(tokens[1])))
	count += 1