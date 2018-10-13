
def main():
	fin = open('A-small-attempt2.in', 'r')#StandingOvationS.in
	fout = open('A-small-attempt.out', 'w')#StandingOvationS.out
	info = fin.read().splitlines()
	reps = int(info[0])
	for n in range(reps):
		data = info[n+1].split()
		smax = int(data[0])
		pcount = data[1]
		totalStanding = 0
		totalAdded = 0
		for i in range(len(pcount)):
			c = int(pcount[i])
			if totalStanding < i and int(pcount[i]) > 0:
				totalAdded = totalAdded + (i-totalStanding)
				totalStanding = totalStanding + totalAdded
			totalStanding = totalStanding+c
		fout.write("Case #"+str(n+1)+": "+str(totalAdded)+"\n")

main()