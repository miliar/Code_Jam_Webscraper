def translate(path):
	inputFile = file(path, "r");
	nLines = inputFile.readline();
	text = inputFile.readlines();
	inputFile.close();
	newPath=path[:path.find(".")+1]+"out";
	outputFile=file(newPath,"w");
	
	gStr1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	gStr2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	gStr3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	gStr4="y qeez\n";
	gStr=gStr1+gStr2+gStr3+gStr4;
	
	eStr1="our language is impossible to understand";
	eStr2="there are twenty six factorial possibilities";
	eStr3="so it is okay if you want to just give up";
	eStr4="a zooq\n";
	eStr=eStr1+eStr2+eStr3+eStr4;
	
	#geDict=buildDictionary(gStr,eStr);
	geDict={};
	for i in range(len(gStr)):
			geDict[gStr[i]]=eStr[i];
	
	k=1;
	for gLine in text:
		eLine=str();
		for i in range(len(gLine)):
			eLine+=geDict[gLine[i]];
			
		outString="Case #"+str(k)+": "+eLine;
		outputFile.write(outString.replace('\'',''));
		k+=1;
	outputFile.close();
	
	
	def buildDictionary(sourceStr,targetStr):
		newDict = {};
		for i in range(len(sourceStr)):
			newDict[sourceStr[i]]=targetStr[i];
		return newDict ;
