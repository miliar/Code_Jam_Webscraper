# Import modules
import re
import math

# Format input
inputname='A-small-attempt0Magic.in'
inputstring=''.join(['/Users/justinsumner/Downloads/',inputname])
inputfile=open(inputstring,'r')
input=[line for line in inputfile]

outputname=''.join([inputname.rstrip('in'),'out'])
outputstring=''.join(['/Users/justinsumner/Documents/codeJam/',outputname])
output=open(outputstring,'w')


T=int(input[0].strip())
inCases=[]
j=1
while j<len(input):
	first=input[j+int(input[j])].split()
	second=input[j+5+int(input[j+5])].split()
	case=[first,second]
	inCases.append(case)
	j+=10


assert len(inCases)==T

# Define method

def inout(x):
	total=0
	for digit in x[0]:
		if digit in x[1]:
			total+=1
			answer=digit
	if total==0:
		return 'Volunteer cheated!'
	if total==1:
		return answer
	if total>1:
		return 'Bad magician!'

# Format output
j=1
for x in inCases:
	print x
	print inout(x)
	case=''.join(['Case #',str(j),': '])
	newline=''.join([case, inout(x),'\n'])
	output.write(newline)
	j+=1

output.close()