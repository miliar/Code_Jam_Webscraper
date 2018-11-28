def Judges(path):
	inputFile = file(path, "r");
	nLines = inputFile.readline();
	rounds = inputFile.readlines();
	inputFile.close();
	newPath=path[:path.find(".")+1]+"out";
	outputFile=file(newPath,"w");
	
	# read opposing 
	
	k=1;
	for curRound in rounds:
		parts=curRound.split();
		# read combinations
		n = int(parts[0]);
		nSurprising = int(parts[1]); 
		roundMin = int(parts[2]); 
		
		if roundMin==0:
			minEquivocalScore = 0;
			minSurprisingScore = 0;
		elif roundMin==1:
			minEquivocalScore = 1;
			minSurprisingScore = 1;
		else:
			minEquivocalScore = 3*roundMin-2;
			minSurprisingScore = 3*roundMin-4;
		
		goodScores=0;
		
		for i in range(3,3+n):
			score = int(parts[i]);
			if score >= minEquivocalScore:
				goodScores+=1;
			elif score >= minSurprisingScore and nSurprising > 0:
				nSurprising-=1;
				goodScores+=1;				
		
		outString="Case #"+str(k)+": "+str(goodScores)+"\n";
		outputFile.write(outString.replace('\'',''));
		k+=1;
	outputFile.close();	
