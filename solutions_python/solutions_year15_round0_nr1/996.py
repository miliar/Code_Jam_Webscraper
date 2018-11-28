

def getMin(line, sMax, i):
	res = 0
	cont = 0
	#print line
	for x in range(sMax+1):
		p = int(line[x])
		#print 'Cont ',cont, 'Res',res
		if cont + res< x:
			res+=x-cont-res
		cont+=p

	return 'Case #%d: %d \n'%(i,res) 

f = open('big.in','r')
lines = f.read().split('\n')
f.close()

f = open('big.out','w')

T = int(lines[0])
for x in range(T):
	i = x+1
	sMax, line = lines[i].split(' ')
	f.write( getMin(line, int(sMax), i) )

f.close()


