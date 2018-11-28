

def main():
	T = int(raw_input())

	for test in range(T):
		[sMax, people] = raw_input().split()
		sMax = int(sMax)
		people = (map(int,list(str(people))))
		
		clappers = 0
		friends = 0

		for i in range(sMax + 1):
			while (clappers < i):
				friends += 1
				clappers += 1
			clappers += people[i]
			
		print ("Case #" + str(test+1) + ": " + str(friends))

main()