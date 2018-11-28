def squareIsPossible(lawn,x,y):
	squareColumn=[]
	for i in range(len(lawn)):
		squareColumn.append(lawn[i][x])
	if len(set(squareColumn))==1 or lawn[y][x]==max(squareColumn):
		return True
	if len(set(lawn[y]))==1 or lawn[y][x]==max(lawn[y]):
		return True
	return False
def isPossible(lawn):
	for y in range(len(lawn)):
		for x in range(len(lawn[0])):
			if not squareIsPossible(lawn,x,y):
				return 'NO'
	return 'YES'
lines=open('B-large.in','r').readlines()[1:]
for i in range(len(lines)):
	lines[i]=lines[i].replace('\n','')
out=open('large_output.txt','w')
curCase=1
i=0
while i<len(lines):
	height=int(lines[i].split()[0])
	lawn=[[]]*height
	for q in range(height):
		lawn[q]=[int(p) for p in lines[i+q+1].split()]
	i+=height+1
	out.write(('Case #{0}: '+isPossible(lawn)+'\n').format(curCase))
	curCase+=1