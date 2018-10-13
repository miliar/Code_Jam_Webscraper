# I/O file names without extension
IN = OUT = 'A-large'

# I/O file names with extension
infile  = IN + '.in'
outfile = OUT + '.out'

# opening I/O files
InFILE  = open(infile, 'r')
OutFILE = open(outfile, 'w')

# Get no. of test cases
T = int(InFILE.readline().strip('\n'))

# Main Body
for case in range(T):
	S_K = InFILE.readline().strip('\n').split()
	S = list(S_K[0])
	K = int(S_K[1])
	B_count = S.count('-')
	min_no_of_flips = 0;
	if(B_count==0):
		OutFILE.write('Case #'+str(case+1)+': '+ str(min_no_of_flips) +'\n')
	else:
		new_S = list(S)
		for pos in range(len(S)):
			if (new_S[pos]=='-' and pos+K <= len(S)):
				for j in range(K):
					if new_S[pos+j] == '+':
						new_S[pos+j] = '-'
					else:
						new_S[pos+j] = '+'
				min_no_of_flips+=1
				if new_S.count('-')==0:
					break
		if min_no_of_flips > 0 and new_S.count('-')==0:
			# output will be as 'Case #<case_no>: <output>\n'
			OutFILE.write('Case #'+str(case+1)+': '+ str(min_no_of_flips) +'\n')
		else:
			# output will be as 'Case #<case_no>: <output>\n'
			OutFILE.write('Case #'+str(case+1)+': IMPOSSIBLE\n')
# End

#close I/O files
InFILE.close()
OutFILE.close()
