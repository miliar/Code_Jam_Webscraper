from re import findall
def find(pic):
	y=0
	v=1
	output=''
	for l in range(len(pic)):
		if '#' in pic[l]:
			for ll in range(len(pic[l])):
				y=0
				if pic[l][ll]=='#':
					y=ll
					if ll!=len(pic[l])-1 and l!=len(pic)-1:
						if pic[l][y] == '#' and pic[l][y+1] == '#' and pic[l+1][y] == '#' and pic[l+1][y+1] == '#':
							pic = replace(pic, l, y)
					else:
						v=0
						pass
	for l in range(len(pic)):
		if '#' in pic[l]:
			v=0
			break
	if v==1:
		for l in range(len(pic)):
			for ll in range(len(pic[l])):
				output+=pic[l][ll]
			output+='\n'
		return output
	else:
		return 'Impossible\n'
def replace(pic, r, c):
	edit=[]
	#set edit
	for l in range(len(pic)):
		edit.append(pic[l])
	#change
	y='\ '
	edit[r][c]='/'
	edit[r][c+1]='\\'
	edit[r+1][c]='\\'
	edit[r+1][c+1]='/'
	return edit
#main
file='large'
i=open(file+'.in', 'r')
o=open(file+'.out', 'w')
cases=int(i.readline())
output=''
for c in range(cases):
	print c
	output+='Case #'+str(c+1)+': \n'
	rows=int(i.readline().split(' ')[0])
	pics=[]
	pic=[]
	for r in range(rows):
		pics.append(i.readline()[:-1])
	for r in range(rows):
		pic.append(findall('.', pics[r]))
	final=find(pic)
	output+=final
o.write(output)