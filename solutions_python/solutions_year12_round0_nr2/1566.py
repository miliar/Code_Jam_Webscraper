import math

def checksurprise(r):
	if math.fabs(r[0] - r[1]) == 2 or math.fabs(r[1]-r[2]) or math.fabs(r[0]-r[2])==2:
		return True
	return False

def makesurprise(l):
	if l[2]==0:
		return l,False
	ls = [l[0],l[1]-1,l[2]+1]
	if checksurprise(ls):
		return ls,True
	else:
	 return l,False
	
def googlerda():
	input=open("B-large.in","r")
	output=open("op.txt","w")
	numb = input.readline()
	numb = int(numb)
	for i in range(0,numb):
		st = input.readline()
		qu = st.split()
		qu = [int(lk) for lk in qu]
		l = qu[3:]
		l.sort()
		l.reverse()
		li = []
		count = 0
		for j in range(0,qu[0]):
			num = l[j]/3
			if num * 3 == l[j]:
				li += [[num,num,num]]
			else:
				lic = [l[j]-(2*num+1),num+1,num] 
				lic.sort()
				li += [lic]
		j,k=0,0
		firsttrial = True
		while j<qu[1]:
			if k>=len(li):
				break
				firsttrial = False
			if li[k][2]==10 and firsttrial:
				k= k+1
			else:
				if(checksurprise(li[k])):
					k= k+1
				else:
					if max(li[k])>=qu[2] and firsttrial:
						k = k+1
						continue
					li[k],made=makesurprise(li[k])
					if made:
						j = j+1
					k= k+1
		for each in li:
			if max(each) >=qu[2]:
				count +=1
		d= int(i)+1
		output.write("Case #"+str(d)+": "+str(count)+"\n")
googlerda()