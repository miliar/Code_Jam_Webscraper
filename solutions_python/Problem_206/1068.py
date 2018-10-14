	

# Import the file as a list of lines:

# def sortString(stringArr):	
# 	output=[];
# 	return output;



file_in = 'in.txt'
file_out = 'out.txt'

with open(file_in,'rb') as fin, open(file_out,'wb') as fout:
	
	lines = fin.read().splitlines()
	case = 1
	cases=int(lines[0])
	lines=lines[1:]
	index=0;

	for i in range(cases):
		case = i+1
		rC=lines[index].split();

		d=int(rC[0]);
		n=int(rC[1]);
		index=index+1;
		t1=0;
		for j in range(n):
			ps=lines[index].split();
			p=int(ps[0]);
			s=int(ps[1]);

			tempT=(d-p)/float(s);
			t1=max(t1,tempT);
			index=index+1;
		speed=d/t1;

		speed='{0:.6f}'.format(speed)
		
		output = 'Case #%d: %s\n' % (case,speed)
		
		# output=str(r);
		# fout.write(output)
		# index=index+n; 

		


		fout.write(output)
		
		

	# print (lines)

		







