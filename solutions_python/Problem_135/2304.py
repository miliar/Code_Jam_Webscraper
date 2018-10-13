def readfile():
	with open('input.in', 'r') as f:
		data = f.readlines()
		numTest = int(data[0])
		w = open('output.ou','w')
		for i in range(numTest):
			f = i * 10 + 1
			to = f + 10
			test = data[f:to]
			print test
			result = list(analyze(test))
			pos = i + 1
			r = "Case #"+str(pos) + ":"
			if len(result) == 0:
				r = r + " Volunteer cheated!\n"
				w.write(r)
			elif len(result) > 1:
				r = r + " Bad magician!\n"
				w.write(r)
			elif len(result) == 1:
				r = r + " " +str(result[0]) +"\n"
				w.write(r)
			print "=========================="
		w.close()
	return 1

def analyze(input):
	numRow1 = int(input[0])
	numRow2 = int(input[5])
	square1 =[input[1].split(),input[2].split(),input[3].split(),input[4].split()]
	square2 = [input[6].split(),input[7].split(),input[8].split(),input[9].split()]
	a =  square1[numRow1-1]
	b = square2[numRow2-1]
	result = set(a).intersection(b)
	return result
if __name__ == "__main__":
	print readfile()