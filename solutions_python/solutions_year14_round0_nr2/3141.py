# Import modules
import re
import math

# Format input
inputname='B-large.in'
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
	case=[float(k) for k in input[j].split()]
	inCases.append(case)
	j+=1

assert len(inCases)==T

# print T, len(inCases)

print inCases

# Define method

def inout(c, f, x):
	speed=2.0
	elapsed=0.0
	for i in range(int(x)):
		if x/speed < c/speed+x/(speed+f):
			elapsed+=x/speed
			return elapsed
		else:
			elapsed+=c/speed
			speed+=f



# Format output
j=1
for x in inCases:
	print x
	print inout(x[0], x[1], x[2])
	case=''.join(['Case #',str(j),': '])
	newline=''.join([case, str(inout(x[0], x[1], x[2])),'\n'])
	output.write(newline)
	j+=1

output.close()