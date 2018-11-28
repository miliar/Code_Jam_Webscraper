import copy,re,sys


def process_data(filename,opfile):
	f=open(filename)
	fout=open(opfile,'w')
	cases, currcase,lineno=0,0,0
	for line in f:
		lineno+=1
		line=line.strip()
		if(lineno==1):
			cases=int(line)
			continue
		currcase+=1
		print currcase
		num= line
		ans=next_num(num)
		fout.write('Case #%d: %s\n'%(currcase,ans))
		fout.flush()
	f.close()
	fout.close()



#assume n is passsed in as a string
#remember to handle single digit case specially
def nlex(n):
	
	narr=map(lambda(x):int(x),list(n))
	m=-1
	for i in range(len(narr)-1):
		if(narr[i]<narr[i+1]):m=i
	if(m==-1):return n,False
	
	
	am=narr[m]
	bm,bmidx=min([(narr[idx],idx) for idx in range(m+1,len(narr)) if(narr[idx]>am) ])
	#print m,am,bm
	del narr[bmidx]
	a_new=copy.copy(narr[m+1:])
	a_new.append(am)
	a_new.sort()
	narr[m]=bm
	del narr[m+1:]
	#print narr
	narr+=a_new
	return  ''.join(map(lambda(x):str(x),narr)), True

#return next string			
def next_num(n):
	a,stat = nlex(str(int(n)))
	if(stat==False):
		ar=list(a)
		while(True):
			if(ar[-1]=='0'):del ar[-1]
			else: break
		ar.reverse()
		while(True):
			if(len(ar)==len(n)+1):break
			ar.insert(1,'0')
		
		return ''.join(ar)
	else:return a
