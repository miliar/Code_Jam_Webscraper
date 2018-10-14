
def main():
	infile = open('P1.in')
	outfile = open('P1.out', 'w')
	n = int(infile.readline())
	ans1 = 1
	ans2 = 2
	for j in range (0,n):
		res1 = int(infile.readline())
		x = 1		
		while x < 5: 
			r = infile.readline()
			if x == res1:
				ans1 = r.split()
			x = x+1

		res2 = int(infile.readline())
		x = 1		
		while x < 5: 
			r = infile.readline()
			if x == res2:
				ans2 = r.split()
			x = x+1

		result = "Volunteer cheated!"
		found = False
		for i in ans1:
			if i in ans2:
				if found == True:
					result = "Bad magician!"
				else:
					found = True
					result = i
		res = "Case #%d: %s \n" % (j+1, result)
		outfile.write(res)
		print res

	infile.close()
	outfile.close()


main()