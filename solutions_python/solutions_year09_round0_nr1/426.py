#/usr/bin/env python 
import sys, re


def splitToken(pat):
	start = 0
	string = ""
	token = []
	for i in range(len(pat)):
		if(pat[i] == '('):
			start = 1
		elif(start == 1):
			if(pat[i] == ')'):
				token.append(string)	
				string = ""
				start = 0
			else:
				string += pat[i]
		else:
			token.append(pat[i])
	
	return(token)
			
			

		

def processTokens(pat,hash):

	# first split them 
	token = re.findall('[a-zA-Z]+',pat)
	if(len(token) == 1): 
		token = re.findall('[a-zA-Z]',token[0])
	
	
	# calculate score 
	Score = []
	nTokens = len(token)
	for i in range(nTokens):
		sc = 0
		nChars = len(token[i])
		for j in range(nChars):
			try:
				sc += hash[i][token[i][j]]
			except:
				sc += 0
		Score.append(sc)

	print Score 
	index = Score.index(min(Score))
	print index
	print token
	print	token[index]
		
	return min(Score)



def test(patterns, pat):
	total = 0


	#token = re.findall('[a-zA-Z]+',pat)
	#if(len(token) == 1): 
	#	token = re.findall('[a-zA-Z]',token[0])
	#print token
	token = splitToken(pat)
	#print token
	for pp in patterns:
		#print pp
		flag = 1
		#print len(pp)
		for j in range(len(pp)):
			#print token[j]
			if(pp[j] not in token[j]):
				flag = flag *0
		if(flag):
			total += 1

	return(total)	
			

		
	


	


def process(infile):
	fp = open(infile)
	data = fp.readlines()
	fp.close()

	# read frst line 
	firstline = data[0].split(" ")
	nChars = int(firstline[0])
	nWords = int(firstline[1])
	nPatterns = int(firstline[2])
	
	#print nChars, nWords, nPatterns	
	
	Words = []
	# Process Language 
	hash = []
	for i in range(nChars):
		temp = {}
		hash.append(temp)
			
	count = 0		
	for i in range(1,nWords+1):
		count += 1
		Words.append(data[i].strip())
		for j in range(nChars):
			try:
				hash[j][data[i][j]] += 1		
			except:
				hash[j][data[i][j]] = 1		
	
	#print count
	#for line in hash:
	#	print line 
	
	#print Words
	#Process inputs 
	for i in range(nPatterns):
		pat = data[nWords+i+1].strip()
		#print pat	
		string = "Case #"+str(i+1)+":"
		print string, test(Words,pat)
		#print string, processTokens(pat,hash)
		#print "---------------------------------"
		







			




if(__name__=="__main__"):
	process(sys.argv[1])
