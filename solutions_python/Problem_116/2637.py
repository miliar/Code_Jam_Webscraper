linestring = open('inputing', 'r').readlines()
f = open('myfile','w')
a=1
b=5
size=int(linestring[0])
for being in range(size): 
	s=''
	t=''
	xa=''
	new=linestring[a:b]

	for i in range(4):
		xo=''
		for j in range(4):
			if i==j:
			   s+=new[i][j]
			if i+j==3:
			   t+=new[i][j]
			xo+=new[j][i]
			xa+=new[i][j]
		new.append(xo+'\n')

	new.append(s+'\n')	
	new.append(t+'\n')
	new.append(xa+'\n')
	
	if(('OOOT\n' in new) or ('OOOO\n' in new) or ('TOOO\n' in new)):
		f.write('Case #{}: O won'.format(being+1)+'\n')
	elif (('XXXT\n' in new) or ('XXXX\n' in new) or ('TXXX\n' in new)):
		f.write('Case #{}: X won'.format(being+1)+'\n')
	else:
		if ('.' in new[len(new)-1]):
			f.write('Case #{}: Game has not completed'.format(being+1)+'\n')
		else:
			f.write('Case #{}: Draw'.format(being+1)+'\n')
	a=b+1
	b=a+4

f.close()
