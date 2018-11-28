def solve(naomi,ken,n):


	naomi.sort()
	naomi.reverse()
	ken.sort()
	score = 0

	naomi_returns = [x for x in naomi]
	ken_returns = [x for x in ken]

	for x in range(n):
		if ken[-1] < naomi[0]:
			ken = ken[1:]
			naomi = naomi[1:]
			score += 1
		else:
			for j in range(len(ken)):
				if ken[j] > naomi[0]:
					k = ken[:j]
					k.extend(ken[j+1:])
					naomi = naomi[1:]
					ken = k
					break
		
		
	print "Genuine: " + str(score)
	original = score
	score = 0

	naomi = naomi_returns
	naomi.reverse()
	ken = ken_returns


	print "Naomi"
	print naomi
	
	print "Ken"
	print ken


	for x in range(n):
		if naomi[0] < ken[0]:
			ken = ken[:-1]
			naomi = naomi[1:]
		else:
			ken = ken[1:]
			naomi = naomi[1:]
			score += 1
		print naomi
		print ken
		print "\n"
				
	print "Deciet: " + str(score) + "\n\n\n\n"
	

	return str(score) + " " + str(original)


f = open("D-large-in.txt","r")
d = f.read().split("\n")
n = int(d[0])

g = open("D-large-out.txt","w")

j = 1
for i in range(1,n+1):
	stuff = d[j+1:j+3]
	naomi = [float(x) for x in stuff[0].split(" ")]
	ken = [float(x) for x in stuff[1].split(" ")]
	ans = solve(naomi,ken,int(d[j]))
	j = j + 3
	# solve(R,C,M,i)

	g.write ("Case #" + str(i) + ": " + ans + "\n")