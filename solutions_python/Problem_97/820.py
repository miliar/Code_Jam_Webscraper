import math


f = open('input.txt')
samples = int(f.readline().strip())
output = ''
for k in range(samples):
	
	string = f.readline().strip().split(' ')
	data = [int(x) for x in string]
	A = data[0]
	B = data[1]
	count = 0
	for i in range(A,B+1):
		for j in range(i+1,B+1):
		#for j in range(pow(10,int(math.log10(A))-1),min(B,pow(10,int(math.log10(A))))):
			si = str(i)
			sj = str(j)
			#print si, sj
			for l in range(1,len(si)):
				if si[l:]+si[:l] == sj and si[l:][0] != 0:
					#print si, sj
					count +=1
					break
	'''
	string = f.readline().strip().split(' ')
	data = [int(x) for x in string]
	A = data[0]
	B = data[1]
	count = 0
	length = len(A)
	for i in range(1,length+1):
	'''
	print k
	output += 'Case #' + str(k+1)+': ' + str(count) + '\n'
o = open('output.txt', 'w')
o.write(output)
o.close
print output
#print diction
#has = []

#for i in diction:
#	has.append(diction[i])
#has.sort()
#needs q
#print has
