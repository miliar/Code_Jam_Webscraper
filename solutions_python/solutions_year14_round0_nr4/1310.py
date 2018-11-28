import sys

filename = sys.argv[1]

sys.stdin = open(filename,'r')
numOfCases = int(raw_input())

for x in range(1, numOfCases+1):
	N = int(raw_input())
	naomi = []
	ken = []
	naomistr = raw_input().split()
	kenstr = raw_input().split()
	for y in range(0, N):
		naomi.append(naomistr[y])
	for y in range(0, N):
		ken.append(kenstr[y])
	naomi.sort(reverse=True)
	ken.sort(reverse=True)

	
	#Deceitful war
	deceitfulPoints = 0
	z = 0
	y = 0
	while y <= N - 1:
		if z == N - 1:
			if naomi[y] > ken[z]:
				deceitfulPoints+=1
			break
		else:			
			if naomi[y] > ken[z]:
				deceitfulPoints+=1
				y+=1
			z+=1
	normalPoints = 0
	z1 = 0
	z2 = N-1
	for y in range(0, N):
		if naomi[y] > ken[z1]:	
			normalPoints+=1		
			z2-=1
		else:
			z1+=1
	print "Case #" + str(x) + ": " + str(deceitfulPoints) + " " + str(normalPoints)
				
		
