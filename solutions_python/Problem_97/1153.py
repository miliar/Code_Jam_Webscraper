def main(args):
	s="adfa";
	translate(args);

def translate(path):
	inputFile = file(path, "r");
	nLines = inputFile.readline();
	numberPairs = inputFile.readlines();
	inputFile.close();
	newPath=path[:path.find(".")+1]+"out";
	outputFile=file(newPath,"w");
	
	k=1;
	for numberPair in numberPairs:
		nums=numberPair.split();
		a=int(nums[0]);
		b=int(nums[1]);
		count=0;
		for i in range(a,b):
			nStr=str(i);
			numDict=[];
			for j in range(len(nStr)-1):
				mStr=nStr[j+1:]+nStr[0:j+1];
				mInt=int(mStr);
				if mInt>i and mInt<=b and (mStr not in numDict):
					count+=1;
					numDict.append(mStr);
				
			
		outString="Case #"+str(k)+": "+str(count)+"\n";
		outputFile.write(outString.replace('\'',''));
		k+=1;
	outputFile.close();
	

	
#path="D:\\My Documents\\CodeJam\\2012\Qualification\\RecycledNumbers\\sampleInput.in"
path="D:\\My Documents\\CodeJam\\2012\Qualification\\RecycledNumbers\\C-small-attempt0.in"
main(path);
