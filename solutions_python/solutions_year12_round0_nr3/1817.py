
inputCount = int(raw_input())


input = []

for i in xrange(0,inputCount):
	input.append(raw_input().split(' '))


def CalculateRecycleNo(x, inB):
	count = 0
	n = str(x)
	length = len(n)

	for letter in xrange(1, length):
		m = n[-letter:] + n[:-letter]
		intM = int(m)
		if(m[0] != '0') and (x < intM <= inB):
			#print("found:" + n +':' + m)
			count+=1
	return count

inputNo = 1
for i in input:
	count = 0
	A = int(i[0])
	B = int(i[1])
	for x in range(A, B ):
		count+=(CalculateRecycleNo(x, B))
	

	print("Case #" + str(inputNo) + ": " + str(count))
	inputNo += 1