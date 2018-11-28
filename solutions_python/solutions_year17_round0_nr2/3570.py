
inData  = open('small.in','r')
outData = open('small.out','w')

lines = int(inData.readline())

def check(data):
	for i in range(len(data)-1):
		if data[i] > data[i+1]:
			return True
	return False

# for line in range(1,lines+1):
# 	numL = list(inData.readline())[:-1]
# 	num = int(''.join(numL))
# 	if num <= 9:
# 		outData.write('Case #%d: %d\n' % (line,num))
# 		continue
# 	while check(numL):
# 		print numL
# 		for i in range(len(numL)-1):
# 			if numL[i] <= numL[i+1]:
# 				continue
# 			else:
# 				num = num - 10 ** (len(numL)-i-1)
# 				numL[:i+1] = list(str(num))[:i+1]
# 				numL[i+1:] = '9'*(len(numL)-i-1)
# 				print num, ' ', numL

# 	outData.write( 'Case #%d: %d\n' % ( line,int(''.join(numL)) ) )	

for line in range(1,lines+1):
	numL = list(inData.readline())[:-1]
	num = int(''.join(numL))
	if num <= 9:
		outData.write('Case #%d: %d\n' % (line,num))
		continue
	while check(numL):
		num -= 1
		numL = list(str(num))

	outData.write( 'Case #%d: %d\n' % ( line,int(''.join(numL)) ) )	

inData.close()
outData.close()

