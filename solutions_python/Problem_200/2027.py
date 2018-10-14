with open("input.txt","r") as file:
	lines=file.read().splitlines()
line_n=0
outlines=[]
t=int(lines[line_n])
line_n=line_n+1
for i in range(t):
	input = map(int,list(lines[line_n]))
	line_n=line_n+1
	for j in xrange(len(input)-1,0,-1):
		if input[j]<input[j-1]:
			for k in xrange(len(input)-1,j-1,-1):
				input[k]=9
			input[j-1]=input[j-1]-1
	ans="Case #"+str(i+1)+": "+str(int("".join([str(num) for num in input])))
	outlines.append(ans)
with open("output.txt","w") as file:
	for line in outlines:
		file.write(line+"\n")