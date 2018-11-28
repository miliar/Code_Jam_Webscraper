
def main():
	t=int(raw_input())
	for i in xrange(t):
		inputs = raw_input().split()
		smax = int(inputs[0])
		sstr = inputs[1]
		count = 0
		aud = 0
		for j in xrange(len(sstr)):
			val = int(sstr[j])
			while aud < j:
				count += 1
				aud += 1
			aud = aud + val
			#print aud
		
		print "Case #"+str(i+1)+":", count

main()