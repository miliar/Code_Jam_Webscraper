import sys;
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	input=str.split(f.readline())
	length = int(input[0])
	wordcnt = int(input[1])
	tcCount = int(input[2])
	
	dict = []
	for i in range(wordcnt):
		# Read all words in dictionary
		word = f.readline()
		dict.append(word)
	# read test cases
	for j in range(tcCount):
		ans = 0
		#print "Test case: ",(j+1)
		tc = f.readline()
		#print "line = ", tc
		tokenlist = []
		# create token list
		for k in range(length):
			if tc[0] == "(":
				closepos = tc.find(")")
				tokenlist.append(""+tc[1:closepos])
				tc = tc[closepos+1:]
			else:
				tokenlist.append(""+tc[0])
				tc = tc[1:]
		#print "tokenlist = ",tokenlist
		# compute the answer
		for w in dict:
			flag = 1
			for l in range(length):
				c = w[l]
				flag =flag & (tokenlist[l].find(c) >= 0)
			if flag:
				ans = ans + 1
		
		outline = 'Case #'+str(j+1)+': '+str(ans)
		#print outline
		outf.write(outline+'\n');
		
	f.close()
	outf.close()

			
main()

