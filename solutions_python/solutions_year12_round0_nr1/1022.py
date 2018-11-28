import collections
def main():
	fi = open('test.txt', 'r')
	fo = open('result.txt', 'r')
	f = open('A-small-attempt2.in', 'r')
	T = int(fi.readline())
	table = {'q': 'z', 'z': 'q'}
	for lineI in fi:
		lineO = fo.readline()
		wordI = lineI.split()
		wordO = lineO.split()
		for i in range(len(wordI)):
			for j in range(len(wordI[i])):
				if table.has_key(wordI[i][j]) == False:
					table[wordI[i][j]] = wordO[i][j]

	Tf = int(f.readline())
	fout = open('out.txt', 'w')
	k = 1
	for line in f:
		lineOut = "Case #" + str(k) + ": "
		for e in line:
			if e == " " or e == "\n":
				lineOut += e
			elif table.has_key(e):
				lineOut += table[e]
			else:
				lineOut += "_"
		fout.write(lineOut)
		k += 1				
		
if __name__ == "__main__":
	main()
			
	
				
			
