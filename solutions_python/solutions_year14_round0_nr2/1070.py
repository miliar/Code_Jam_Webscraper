#cookie.py - Python 3.2.1

from sys import argv

def sum(c,f,x):
	speed,t,n=2.0,0.0,0
	while True:
		if(t+c/speed+x/(speed+f)>t+x/speed):
			t+=x/speed
			break
		t+=c/speed
		#print(t)
		speed+=f
		n+=1
	return t
	


fin = open(argv[1])
fout = open(argv[1].replace(".in",".out"),'w')
T=int(fin.readline())
for Tt in range(1,T+1):
	c,f,x=map(float,fin.readline().split())
	fout.write('Case #{0}: {1:.7f}\n'.format(Tt,sum(c,f,x)))
	#print(Tt,": ",sum(c,f,x))
	#print('Case #{0}: {1:.7f}\n'.format(Tt,sum2(c,f,x)))

