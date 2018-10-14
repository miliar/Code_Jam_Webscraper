

# Import the file as a list of lines:

def countFlips(sstr, k):
	flag=0
	index=-1;
	for j in range(len(sstr)):
		if sstr[j]=='-' and flag==0:
			flag=1
			index=j
	if flag==0:
		return 0
	else:
		if(index>len(sstr)-k):
			return -1;
		else:
			for l in range(index,index+k):
				if(sstr[l]=='+'):
					sstr[l]='-'
				elif(sstr[l]=='-'):
					sstr[l]='+'
		out=countFlips(sstr,k);
		if(out==-1):
			return -1
		else:
			return 1+out





	

	# tempInt=''.join(sstr);
	# tempInt=int(tempInt);
	# sstr=str(tempInt)
	# sstr=list(sstr)
	
	# if flag==0:
	# 	return sstr

	# else:
	# 	return sortString(sstr)


file_in = 'in.txt'
file_out = 'out.txt'

with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
	
	lines = fin.read().splitlines()
	case = 1
	cases=int(lines[0])
	lines=lines[1:]

	for i in range(cases):
		case = i+1
		sstrK=lines[i].split();
		sstr=sstrK[0];
		k=int(sstrK[1]);
		output = countFlips(list(sstr),k);

		if output==-1:
			output='IMPOSSIBLE'
		else:
			output=str(output)
		
		output = 'Case #%d: %s\n' % (case,output)
		fout.write(output)
		
		

	# print (lines)

		







