import sys
f = open(sys.argv[1])


# D = dist2destination; K,S = initial dist, speed
def time(D, K, S):
	return (D - K)/float(S)

# iterates through all groups (number = T)
groupNum = 0
for group in range(int(f.readline())):
	groupNum += 1
	DN = f.readline().split()
	DN = [int(x) for x in DN]
	
	times = []
	for H in range(DN[1]):
		Hi = f.readline().split()
		Hi = [int(x) for x in Hi]
		times.append(time(DN[0], Hi[0], Hi[1]))

#	print ('DN: ',DN)
#	print('times: ',times)
	print ("Case #", groupNum, ": ", DN[0]/float(max(times)),sep='')

f.close()
		

 
