with open("input.txt","r") as file:
	lines=file.read().splitlines()
out_lines=[]
line_n=0
t=int(lines[line_n])
line_n=line_n+1
for i in range(t):
	string,size = lines[line_n].split(" ")
	line_n=line_n+1
	string=list(string)
	size = int(size)
	length=len(string)
	count=0
	flag=0
	for j in range(length):
		if string[j]=='-':
			if j+size>length:
				flag=1
				out_lines.append("Case #"+str(i+1)+": IMPOSSIBLE")
				break
			for k in xrange(j,j+size):
				if string[k]=='+':
					string[k]='-'
				else:
					string[k]='+'
			count=count+1
	if flag==0:
		out_lines.append("Case #"+str(i+1)+": "+str(count))
with open("output.txt","w") as file:
	for line in out_lines:
		file.write(line+"\n")