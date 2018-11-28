#MAM, Google Code Jam - Round 1C, Problem C

infile = open("C-small-attempt9.in", "r")
outfile = open("output.txt", "w")

numtests = int(infile.readline())

#triangles...
cheatdict = {1:1, 2:2, 3:3, 4:4, 5:4, 6:5, 7:6, 8:6, 9:7, 10:7, 11:8, 12:8, 13:9, 14:9, 15:10, 16:10, 17:11, 18:12, 19:13, 20:14}


for T in range(numtests):

	#Input
	(N, M, K) = map(int, infile.readline().split(' '))

	#Calculations
	answer=0

	N, M = max(N,M), min(N,M)

	area = K+4
	side = area**.5
	if int(side)!=side:
		side = int(side)+1
	side = int(side)

	#catch case with no enclosure possible due to width of 2
	if M<=2:
		answer = K

	#catch case with no enclosure possible since 3x3 not needed
	elif K<=4:
		answer = K

	#catch case where corner fill needed
	elif area>N*M:
		answer+=2*(N-2)+2*(M-2)
		while area>N*M:
			area-=1
			answer+=1

	#Triangles are my bane
	elif M==4:
		answer=cheatdict[K]

	#catch case where can't form optimally large rectangle due to small M
	elif side>M:

		side=M
		while (side*M)<area:
			side+=1

		#catch case where can add 1 stone to corner rather than longer side
		if (side-1)*M +1 == area:
			answer+=1
			side-=1
				
		answer += 2*(side-2)+2*(M-2)

	#"Normal" case where we can draw an optimally large rectangle
	else:
		side2=side


		while(side*(side2-1)>=area):
			side2-=1

		#catch case where can add 1 stone to corner rather than longer side
		if (((side-1)*side2)+1)>=area:
			side-=1
			answer+=1

		answer += (side-2)*2+(side2-2)*2

	#Output
	outfile.write("Case #"+str(T+1)+": ")
	#print answer
	outfile.write("%i" % answer)
	outfile.write("\n")