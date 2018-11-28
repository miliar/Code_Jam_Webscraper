def solve(N):
	digits = [int(x) for x in N]
	fn = False
	for i in range(len(digits)):
		if fn:
			digits[i] = 9
		elif i != len(digits)-1:

			if digits[i] > digits[i+1]:
				digits[i] = digits[i] - 1
				fn = True
			elif digits[i] == digits[i+1]:
				for k in range(i, len(digits)):
					if digits[i] < digits[k]:
						break
					elif digits[i] > digits[k]:
						digits[i] = digits[i]-1
						fn = True
						break



	return int(''.join([str(x) for x in digits]))



def main():

	T = int(raw_input())
	responses = list()
	for t in xrange(T):

		N = raw_input()

		responses.append(solve(N))

	i = 0
	for r in responses:
		i+=1
		print "Case #"+str(i)+": "+str(r)

if __name__ == "__main__":
	main()