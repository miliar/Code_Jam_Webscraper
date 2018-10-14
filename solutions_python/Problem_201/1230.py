with open("test.txt") as fd :

	content = fd.readlines()
	i = 1
	with open('result.txt', 'w') as fr:
		for line in content[1:]:
			N, K = [int(x) for x in line.split()]
			# After 2 hours of reflexion ... Fingers crossed
			while(K > 1) :
				N=(N-(K%2))/2
				K=K/2
			# K now is necessarly equal to 1
			if N%2 == 1:
				mini = N/2
				maxi = N/2
			else:
				mini = N/2 -1
				maxi = N/2
			fr.write("Case #" + `i` + ": " + `maxi` + " " + `mini`+"\n")
			i+=1
