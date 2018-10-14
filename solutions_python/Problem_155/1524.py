nT = input()
for i in range(0,nT):
	string = raw_input()
	sMax = int((string.split())[0])
	audiance = list((string.split())[1])
	#print sMax
	#print audiance
	standing = 0
	required = 0
	for k in range(0,sMax+1):
		if(standing >= k):
			standing = standing + int(audiance[k])
		else:
			required = required + (k-standing)
			standing = standing + (k-standing) + int(audiance[k])

	print 'Case #' + str(i+1) + ': ' + str(required)
