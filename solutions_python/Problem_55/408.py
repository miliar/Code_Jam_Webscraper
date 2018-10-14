if __name__ == "__main__":
	T = int(raw_input())

	fileobj = open("rollercoaster_output.txt","w")
	for each_testcase in range(1,T+1):

		rkn = raw_input().split(' ')
		R = int(rkn[0])
		K = int(rkn[1])
		N = int(rkn[2])
		G = []
		if N !=0:
			groups = raw_input().split(' ')
			G = [ int(i) for i in groups ]

		cost = 0

		for each_round in range(R):
			no_of_persons=0
			count = 0
		
			for i in G:
				if (no_of_persons + i) <= K:
					no_of_persons = no_of_persons + i
					count = count+1
				else:
					break

			cost = cost+ no_of_persons

			for i in range(0,count):
				temp = G.pop(0)
				G.append(temp)

		fileobj.write( "Case #"+str(each_testcase)+": "+str(cost)+"\n")

	fileobj.close()