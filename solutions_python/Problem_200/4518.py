# I/O file names without extension
IN = OUT = 'B-small-attempt0'

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
	tidy = 1
	N = int(InFILE.readline().strip('\n'))
	for i in range(N):
		num = i+1
		S = list(str(num))
		Sorted_S = list(S)
		Sorted_S.sort(key=int)
		if (S == Sorted_S):
			tidy = num
	OutFILE.write('Case #'+str(case+1)+': '+ str(tidy) +'\n')

# End

#close I/O files
InFILE.close()
OutFILE.close()
