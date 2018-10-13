'''
'''

###########################################################
# function defs
###########################################################

def pairs(n):
	s = 1
	for x in range(2,n+1):
		s*=x
	t=s/n/(n-1)
	s/=2
	s/=t
	return s
		

###########################################################
# input
###########################################################

input_file = 'C-small-attempt0.in.txt'
#input_file = 'C-large.in.txt'
input_data = open(input_file,'r').readlines()

###########################################################
# cases
###########################################################

output = ''
num_cases = int(input_data[0])
i = 1
for n in range(num_cases):
	A = int(input_data[i].rstrip().split()[0])
	B = int(input_data[i].rstrip().split()[1])
	i += 1
	
	num_rec=0
	paired_numbers = []
	for x in range(A,B+1):
		m = str(x)
		rnums = []
		if not m in paired_numbers:
			rnums = [m]
			for start in range(1,len(m)):
				if m[start] != '0' and not m[start:]+m[:start] in rnums and A <= int(m[start:]+m[:start]) <= B:
					rnums.append(m[start:]+m[:start])
		if len(rnums) > 1:
			paired_numbers += rnums
			num_rec += pairs(len(rnums))
			#print m, rnums, pairs(len(rnums))

	output += 'Case #%d: %d\n'%(n+1,num_rec)

###########################################################
# output
###########################################################

outfile = open('output_small.txt','w')
#outfile = open('output_large.txt','w')
outfile.write(output)
outfile.close()