f = open('input.txt')
samples = int(f.readline().strip())
output = ''
for k in range(samples):
	
	string = f.readline().strip().split(' ')
	data = [int(x) for x in string]
	N = data[0]
	suprise = data[1]
	asleast = data[2]
	scores = data[3:]
	supriseLeft = suprise
	print string
	count = 0
	almosts = 0
	for score in scores:
		remainder = score%3
		maxScore = 0
		if remainder == 2:
			remainder = 1

		maxScore = score/3+remainder
		#can do it without surprise


		if maxScore >= asleast:
			count += 1
		else:
			remainder = score%3
			maxScore = score/3 + remainder
			if supriseLeft != 0 and maxScore >= asleast:
				supriseLeft -= 1
				count +=1

		remainder = score%3		
		if remainder == 0 and score/3 == asleast-1 and asleast > 1:

			almosts += 1

		print maxScore, supriseLeft
	
	count += min(almosts,supriseLeft)


	#print 'count',count

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
