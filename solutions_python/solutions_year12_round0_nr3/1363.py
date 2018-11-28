input = open("C-large.in","r")
output = open("C-large.out","w")
test_cases = int(input.readline())
for test in range(test_cases):
	A,B = input.readline().split(" ")
	count = 0
	s = set()
	#print "test",test
	n = int(A)
	b = int(B)
	while n < b+1:
		N = str(n)
		for i in range(len(N)-1):
			x = N[i+1:] + N[0:i+1]
			if int(A) <= n < int(x) <= int(B):
				s.add((n,x))
		n += 1
	output.write("Case #%i: %i\n"%(test+1,len(s)))