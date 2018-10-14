def problemA(input):
	StandCount=0
	add=0
	i=0

	input = map(int, input)

	for each in input:

		if i==0:

			StandCount += each
			i += 1

		else:

			if StandCount>=i:

				StandCount += each
				i += 1

			else:

				if each != 0:

					while StandCount < i:

						StandCount += 1
						add += 1

					StandCount += each
					i += 1

				else:

					i += 1


	return add

if __name__ == "__main__":

    testcases = input()
     
    for caseNr in xrange(1, testcases+1):

        cipher = raw_input()

        print("Case #%i: %s" % (caseNr, problemA(cipher[2:])))
