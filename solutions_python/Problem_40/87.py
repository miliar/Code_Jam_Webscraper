inputFile = "A-large.in";
outputFile = "A-large.out";

def main():	
	fdin = open(inputFile);
	fdout = open(outputFile, 'wb');
	
	casecountString = fdin.readline();
	caseCount = int(casecountString);
	
	for k in range(caseCount):
		treelines = int(fdin.readline());
		tokenStr= [];
		for i in range(treelines):
			line = fdin.readline();
			tokens = getTokens(line);
			tokenStr = tokenStr+ tokens;

		tree = build(tokenStr);
		resultLine1 = "Case #" + str(k+1) +":\n";
		fdout.write(resultLine1);
		anilines = int(fdin.readline());
		for j in range(anilines):
			ani = fdin.readline();
			features = ani.split()[2:];
			result = process(tree, features);
			resultLine = "%.7f\n"%result;
			fdout.write(resultLine);

def getTokens(line):
	tokens = line.split();
	index = 0;
	while True:
		if tokens[index][0] == '(' and len(tokens[index])>1:
			temp = tokens[:index];
			temp.append('(');
			temp.append(tokens[index][1:]);
			tokens = temp + tokens[index+1:];
			index = index + 1;
		elif tokens[index][-1] == ')' and len(tokens[index])>1:
			temp2 = tokens[:index];
			temp2.append(tokens[index][:-1]);
			temp2.append(')');
			tokens = temp2 +tokens[index+1:];
		else:
			index = index +1;
		if index >= len(tokens):
			break;
	return tokens;
	
def build(tokens):
	if len(tokens) ==3:
		p=float(tokens[1]);
		f='';
		return [p,f,[],[]];
	else:
		p=float(tokens[1]);
		f=tokens[2];
		counter = 0;
		cut = 0;
		for i in range(3,len(tokens)):
			if tokens[i]== '(':
				counter = counter + 1;
			elif tokens[i]== ')':
				counter = counter - 1;
			if counter == 0:
				cut = i;
				break;
		left = build(tokens[3:cut+1]);
		right = build(tokens[cut+1:-1]);
		return [p,f,left, right];
		
def process(tree, features):
	p=tree[0];
	if tree[1] == '':
		return p;
	if tree[1] in features:
		return p*process(tree[2], features);
	else:
		return p*process(tree[3], features);
			
	
if __name__ == "__main__":
    main()