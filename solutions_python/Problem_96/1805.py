def googlers(fname):
	lines = [line.strip() for line in open(fname)]
	if( int(lines[0]) != int(len(lines)-1)  ):
		print("error: wrong text length")
	else:
		lines = lines[1:]
		outText=""
		for lineIndex in range(len(lines)):
			count=0
			surpCount=0
			numbers = [int(a) for a in lines[lineIndex].split()]
			N=numbers[0]	#number of "Googlers"
			S=numbers[1]	#number of surprising results, where there is a difference of 2
			p=numbers[2]	#threshold max possible score, for a Googler to be counted
			totals = numbers[3:]
			if(N != int(len(totals))  ):
				print("error: wrong text length 2nd clause")
			else:
				for total in totals:
					unsurpScore = (total+2)/3
					if unsurpScore >= p:
						count=count+1
					else:
						if (total > 4) and (((total+4)/3) >= p):
							surpCount= surpCount+1
			if S <= surpCount:
				count = count+S
			else:
				count = count + surpCount
			outText = outText +"Case #"+str(lineIndex+1)+": "+str(count)+"\n"
		outFile = open("out.txt", 'w')
		outFile.write(outText)
		outFile.close()
