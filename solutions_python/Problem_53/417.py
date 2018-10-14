if __name__ == "__main__":
	fileobj = open("snapperchain_output.txt","w")

	T = int(raw_input())

	for each_testcase in range(1,T+1):
		
		input = raw_input()
		inp = input.split(' ')
		N = int(inp[0])
		K = int(inp[1])

		tot = pow(2,N)
		no_of_times = K

		if no_of_times > tot:
			no_of_times = K%tot

		snappers = 0

		if N != 0:
			snappers = snappers + no_of_times

		fin = bin(snappers)
		final = fin[2:len(fin)]
		if len(final) < N:
			diff = N - len(final)
			initial_0s = "0" * diff
			final = initial_0s + final

		get_power=1
		for i in range(0,len(final)):
			if final[i] != '1':
				get_power = 0
				break
		if get_power == 1:
			fileobj.write( "Case #"+str(each_testcase)+": ON\n" )
		if get_power == 0:
			fileobj.write( "Case #"+str(each_testcase)+": OFF\n" )


	fileobj.close()