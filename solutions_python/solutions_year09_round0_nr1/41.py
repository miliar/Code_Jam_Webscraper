inputFile = "A-large.in";
outputFile = "A-large.out";

dict = {};

def main():	
	fdin = open(inputFile);
	fdout = open(outputFile, 'wb');
	
	countString = fdin.readline();
	wordLength = int(countString.split()[0]);
	dicLength = int(countString.split()[1]);
	caseCount = int(countString.split()[2]);
	
	for i in range(dicLength):
		word = fdin.readline();
		insert_dict(word, wordLength);
		
	for k in range(caseCount):
		line = fdin.readline();
		result = processCase(dict, line);
		resultLine = "Case #" + str(k+1) + ": " + str(result) + "\n";
		fdout.write(resultLine);
		
def insert_dict(word, wordLength):
	idict = dict;
	for i in range(wordLength):
		if not idict.has_key(word[i]):
			idict[word[i]]={};
		idict= idict[word[i]];
			
		
def processCase(dic, s):
	if dic == {}:
			return 1;
	if s[0]=='(':
		rightp=s.find(')');
		count=0;		
		for p in range(1, rightp):
			if dic.has_key(s[p]):
				count=count+processCase(dic[s[p]],s[rightp+1:]);
		return count;
	elif dic.has_key(s[0]):
		return processCase(dic[s[0]],s[1:]);
	else:
		return 0;
	

if __name__ == "__main__":
    main()
