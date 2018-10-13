file=open('A-small-attempt0.in')
input=file.read()
file.close()
input=input.split('\n')
input=input[1:-1]
print(len(input))
output=''

file=open('problem 1-dict')
d=eval(file.read())
file.close()

for i in range(len(input)):
	output+='Case #%d: '%(i+1)
	for j in input[i]:
		output+=d[j]
	if i<len(input)-1:
		output+='\n'

file=open('problem 1-output','w')
file.write(output)
file.close()