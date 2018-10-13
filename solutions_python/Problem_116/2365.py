f = open('A-large.in', 'r')
g = open('output.txt','wb')
string=f.read()
f.close()
strList = string.split("\n")
n=strList[0]
b=[]
output=""
for i in xrange(int(n)):
	winner=""
	unfinished=0
	b.append(strList[i*5+1:(i+1)*5])
	for j in xrange(16):
		if b[i][int(j/4)][j%4]=='X':
			b[i][int(j/4)]=b[i][int(j/4)][:j%4]+'2'+b[i][int(j/4)][j%4+1:]
		if b[i][int(j/4)][j%4]=='O':
			b[i][int(j/4)]=b[i][int(j/4)][:j%4]+'3'+b[i][int(j/4)][j%4+1:]
		if b[i][int(j/4)][j%4]=='T':
			b[i][int(j/4)]=b[i][int(j/4)][:j%4]+'1'+b[i][int(j/4)][j%4+1:]
		if b[i][int(j/4)][j%4]=='.':
			b[i][int(j/4)]=b[i][int(j/4)][:j%4]+'0'+b[i][int(j/4)][j%4+1:]
			unfinished=1
	
	for j in xrange(4):
		m=1
		for k in xrange(4):
			m*=int(b[i][j][k])
		if m == 16 or m == 8:
			winner="X"
		if m == 81 or m == 27:
			winner="O"
		m=1
		for k in xrange(4):
			m*=int(b[i][k][j])
		if m == 16 or m == 8:
			winner="X"
		if m == 81 or m == 27:
			winner="O"
	m=int(b[i][0][0])*int(b[i][1][1])*int(b[i][2][2])*int(b[i][3][3])
	if m == 16 or m == 8:
		winner="X"
	if m == 81 or m == 27:
		winner="O"
	m=int(b[i][0][3])*int(b[i][1][2])*int(b[i][2][1])*int(b[i][3][0])
	if m == 16 or m == 8:
		winner="X"
	if m == 81 or m == 27:
		winner="O"
	if unfinished==1 and winner=="":
		output+="Case #"+str(int(i)+1)+": "+"Game has not completed"+"\n"
	elif winner=="":
		output+="Case #"+str(int(i)+1)+": "+"Draw"+"\n"
	else:
		output+="Case #"+str(int(i)+1)+": "+winner+" won"+"\n"
g.write(output)
g.close()
print b[0]
print b[1]
print b[2]
print b[3]
print b[4]
print b[5]
z=input()
