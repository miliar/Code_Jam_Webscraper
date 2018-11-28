def calc_count(line):
	k=line.split(' ')
	if len(k)==1:
		return -1
	numGooglers=int(k[0])
	numSpecial=int(k[1])
	check=int(k[2])
	scores=k[3:]
	count=0
	for score in scores:
		value=int(score)
		if value%3==0:
			val=value/3
			if val >= check:
				count+=1
			elif check-val==1:
				if val-1 > 0:
					if numSpecial >=1:
						count+=1
						numSpecial=numSpecial-1
		if value%3==1:
			val=value/3
			if val >=check:
				count+=1
			elif check-val==1:
				count+=1
		if value%3==2:
			val=value/3
			if val >=check:
				count+=1
			elif check-val==1:
				count+=1
			elif check-val==2 and numSpecial>=1:
				count+=1
				numSpecial=numSpecial-1
	return count
	
if __name__=="__main__":
	FILENAME='/Users/adityajitta/Downloads/B-small-attempt2.in.txt'
	fp=open(FILENAME,'r')
	num=0
	for line in fp:
		count=calc_count(line.strip())
		if count >= 0:
			num+=1
			print "Case #"+str(num)+": "+str(count)