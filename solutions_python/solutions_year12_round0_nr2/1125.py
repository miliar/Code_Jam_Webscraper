def Dance(e,n,s,p):
	if e==0:
		return 0,s
	v = int(e/3)
	if v >=p:
		return 1,s
	sub = e - 3*v
	#print(e,v+sub,p,s)
	#v<p use sub to increase but make sure that the triplet is valid
	if sub==1:
		if (v+sub) >=p:
			return 1,s
	if sub==2:
		if (v+sub-1)>=p:
			return 1,s
		elif (v+sub) >=p:
			if s >0:
				s -=1
				return 1,s
	if s>=1:
		if (v+1)>=p:
			s-=1
			return 1,s
		
	return 0,s

def main():
	f=open("test","r")
	t=int(raw_input())
	for i in range(t):
		a = raw_input().split()
		n=int(a[0])
		s=int(a[1])
		p=int(a[2])
		k=[]
		res=0
		if p==0:
			print("Case #"+str(i+1)+": " +str(n))
		else:
			for j in range(n):
				ele = int(a[3+j])
				k+= [ele]
				r,s = Dance(ele,n,s,p)
				#print(ele,r)
				res+=r
			print("Case #"+str(i+1)+": " +str(res))
	return

if __name__=='__main__':
	main()
