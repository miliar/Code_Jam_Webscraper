infile = open("C:\\Users\\Intrex\\Downloads\\A-large.in", "r")
outfile = open("C:\\Users\\Intrex\\Downloads\\outfile.txt", "r+")

def proba():
	numstanding = 0
	testcases = int(infile.readline())
	casenumber = 1
	needed = 0
	
	while casenumber <= testcases:
		s = infile.readline().split(" ")
		smax = int(s[0])
		audience = s[1]
		
		if smax == 0:
			print("Case #" + str(casenumber) + ": " + str(0))
			outfile.write("Case #" + str(casenumber) + ": " + str(0) + "\n")
			casenumber += 1
			numstanding = 0
			needed = 0
			continue
		else:
			for i in range(len(audience) - 1):
				if numstanding >= i:
					numstanding += int(audience[i])
					continue
				elif numstanding < i:
					addmembers = i - numstanding
					needed += addmembers
					numstanding = numstanding + int(audience[i]) + addmembers
			print("Case #" + str(casenumber) + ": " + str(needed))
			outfile.write("Case #" + str(casenumber) + ": " + str(needed) + "\n")
			casenumber += 1
			numstanding = 0
			needed = 0
	infile.close()
	outfile.close()

if __name__ == '__main__':
	proba()