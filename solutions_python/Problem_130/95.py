f = open('input.txt','r')
f2 = open('output.txt','w')
t = int(f.readline())
for z in range(0,t):
	(N,P) = map(int,f.readline().split())
	p = 2**N-1;
	pos = 0
	while p>=P:
		p -= 2**pos
		pos+=1
	#print pos
	if pos!=0:
		w = 2**(N-pos+1)-2
	else:
		w = 2**N-1
	
	p = 2**N-1;
	pos = N-1
	while p>=P:
		p -= 2**pos
		pos-=1
	k = 2**N-2**(N-pos-1)
	f2.write('Case #' + str(z+1) + ': ' +str(w) + ' ' + str(k) + '\n')