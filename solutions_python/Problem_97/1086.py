from sys import stdin
f = open('output.out', 'w')

for i in range(int(stdin.readline())):
	lineread = stdin.readline().split()
	lower = lineread[0]
	upper = lineread[1]
	
	numRecycled = 0
	for j in range(int(lower), int(upper)+1):
		number = str(j)
		for k in range(len(str(j))):
			lastDigit = number[len(number)-1]
			number = lastDigit+number[0:len(number)-1]			
			if number[0] != '0' and int(number) != j:
				if int(number) >= int(lower) and int(number) <= int(upper):
					#print number
					numRecycled +=1
					
	print 'Case #'+str(i+1)+': ' + str(numRecycled/2)
	f.write('Case #'+str(i+1)+': ' + str(numRecycled/2) + '\n')

f.close()
