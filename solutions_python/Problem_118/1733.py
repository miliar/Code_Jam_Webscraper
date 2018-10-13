import math

def fairsqr(myfile):
	f = open(myfile, "r")
	g = open("file7.out", "w")
	numExamples = int(float(f.readline()))
	k = 1
	while (k < numExamples+1):
		num = 0
		N,M = f.readline().split()
		N = int(float(N))
		M = int(float(M))
		i = N
		while i <= M:
				#check if palindrome
				i = int(i)
				if str(i) == str(i)[::-1]:
					#if palindrome, check if sqrt is palindrome
					n = math.sqrt(i)
					if abs(int(n) - n) == 0:
						n = int(n)
						if str(n) == str(n)[::-1]:
							# if yes, then count
							num += 1
				i += 1
		g.write("Case #" + str(k) + ": " + str(num) + "\n")
		k += 1
	f.close()
	g.close()

print fairsqr('C-small-attempt0.in')
