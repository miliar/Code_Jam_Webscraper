fi = open("A-large.in","r")
T = int(fi.readline())

def parseAudience(audience):
	result = []
	for i in range(len(audience)):
		result.append(int(audience[i]))
	return result


def minimumToInvite(audience):
	#sum of all prev positions >= current index number
	audience = parseAudience(audience)
	toInvite = []
	prevSum = 0
	for i in range(len(audience)):
		toInvite.append(max(0,i-prevSum))
		prevSum += (audience[i]+toInvite[i])
	return sum(toInvite)

fo = open("output.txt","w")
for t in range(T):
	testcase = fi.readline().split()
	result = minimumToInvite(testcase[1])
	print ("Case #%i: %i"%(t+1,result))
	fo.write("Case #%i: %i\n"%(t+1,result))
fi.close()
fo.close()
