nt = input()
output = {4:{4:{4:'G',3:'R',2:'G'},3:{4:'G',3:'G',2:'G'},2:{4:'R',3:'R',2:'G'},1:{4:'R',3:'R',2:'G'}},3:{3:{4:'R',3:'G',2:'R'},2:{4:'R',3:'G',2:'G'},1:{4:'R',3:'R',2:'R'}},2:{2:{4:'R',3:'R',2:'G'},1:{4:'R',3:'R',2:'G'}},1:{1:{4:'R',3:'R',2:'R',1:'G'}}}
for i in range(0,nt):
	string = raw_input()
	x = int(string.split()[0])
	r = int(string.split()[1])
	c = int(string.split()[2])
	#print x
	#print r
	#print c
	if x == 1:
		print 'Case #' + str(i+1) + ': GABRIEL'
	else:
		if r < c:
			(r,c) = (c,r)
		if(output[r][c][x] == 'G'):
			print 'Case #' + str(i+1) + ': GABRIEL'
		else:
			print 'Case #' + str(i+1) + ': RICHARD'

