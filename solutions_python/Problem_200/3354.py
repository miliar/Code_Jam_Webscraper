import sys
import time

#def eprint(*args, **kwargs):
#	print(*args, file=sys.stderr, **kwargs)

#start_time=time.time()
lines=[]
for line in sys.stdin:
	lines.append(line.strip('\n'))

nb=int(lines[0])
for nb_l in range(nb):
	N=int(lines[nb_l+1])
	num=list(str(N))
	num.reverse()
	ok=0
	while(ok==0):
		n_max=9
		ok=1
		for i,n in enumerate(num):
			if(int(n)>n_max):
				ok=0
				num[i]=str(int(num[i])-1)
				for j in range(0,i):
					num[j]="9"
				break
			else:
				n_max=int(n)
	num.reverse()
	print("Case #{}: {}".format(nb_l+1,int(''.join(num))))
#	N=int(data[0])
#	K=int(data[1])
#	branch=list(str('{0:b}'.format(K)))
#	N2=N
#	if(N2%2==0):
#		ls=int(N2/2-1)
#		rs=int(N2/2)
#	else:
#		ls=int(N2/2)#acts as a floor
#		rs=int(N2/2)#acts as a floor
#	for step in branch[1:]:
#		if(step=='0'):
#			N2=rs
#		else:
#			N2=ls
#		if(N2%2==0):
#			ls=int(N2/2-1)
#			if(ls<0):
#				ls=0
#			rs=int(N2/2)
#		else:
#			ls=int(N2/2)#acts as a floor
#			rs=int(N2/2)#acts as a floor
#	print("Case #{}: {} {}".format(nb_l+1,max(ls,rs),min(ls,rs)))
	
	
#print(time.time()-start_time)
