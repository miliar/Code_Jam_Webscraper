import fileinput


if __name__ == "__main__":
	
	f = fileinput.input()
	T = int(f.readline())

	for case in range(1, T+1):
		N = f.readline().strip('\n')
		#print "N: " + N + "  len(N): "+ str(len(N))
		
		outStr = ""

		refPt = 0
		changeNum = False


		if int(N) < 10: 
			outStr = N

		else: 
			for i in range(0,len(N)-1):	
				if N[i] > N[i+1]:
					changeNum = True
					break

				if N[i] < N[i+1]:
					refPt = i+1


			if changeNum:
				for i in range(0,len(N)):
					#print "i: " + str(i) + "  N[i]: " + N[i]
				
					
					if i > refPt:
						outStr = outStr + "9"
					elif i == refPt:
						if i == len(N)-1:
							outStr = outStr + N[i]

						else:
							if int(N[i]) > 1:
								outStr = outStr + str(int(N[i])-1)
					else:
						outStr = outStr + N[i]
			else:
				outStr = N


					


		print("Case #{0}: {1}".format(case, outStr))
