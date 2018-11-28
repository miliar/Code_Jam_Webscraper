
fin = open("in.txt","r")


N = int(fin.readline())


f = open( "out.txt","w")


for T in range(N):
	(smax,shyness_list) = fin.readline().split()
	t = 0
	friends = 0
	for k, no_of_people in enumerate(shyness_list):
		no_of_people = int(no_of_people)
		if k>t and no_of_people != 0:
			r = k-t
			t+=r
			friends += r
		t+=no_of_people
	f.write("Case #{}: {}\n".format(T+1,friends))


f.close()

fin.close()