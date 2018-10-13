import fileinput

f = open('A-large.in', 'r')

T = f.readline()

for i in range(0,int(T)):
	TC = f.readline()
	Smax, crowd = TC.split()
	crowd = crowd.strip()
	ppl_so_far=int(crowd[0])
	friends_needed=0
	for j in range(1,int(Smax)+1):
		if ppl_so_far+friends_needed<j and int(crowd[j])>0:
			friends_needed+=(j-(ppl_so_far+friends_needed))
		ppl_so_far+=int(crowd[j])
		if ppl_so_far>int(Smax):
			break

	print "Case #" + str(i+1) + ": " + str(friends_needed)
