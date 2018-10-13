from sys import stdin
def comb(a):

	countador=0
	aux=0
	aux2=0

	for z in range(0,n+2):
		if a[z]==0 :
			countador+=1
		else :
			countador=0
		if countador>aux :
			aux=countador
			aux2=z
		kell4gs=aux2-(aux//2)
	return kell4gs
def aqwe(kiwi,choco,a):
	b3=0
	chock=choco-1
	choca=choco+1
	lr=0
	ll=0
	while b3==0:
		if a[chock]==0 :
			ll+=1
			chock-=1
			b3=a[chock]
		else:
			break
	b3=0
	while b3==0 :
		if a[choca]==0 :
			lr+=1
			choca+=1
			b3=a[choca]
		else:
			break
	if ll >= lr :
		maxs=ll
		mins=lr
	else :
		maxs=lr
		mins=ll

	print("Case #"+str(kiwi+1)+": "+str(maxs)+" "+str(mins))
	
t=stdin.readline().strip()
t=int(t)
for kiwi in range(0,t):
	nk=stdin.readline().strip().split()
	a=[1]
	n=nk[0]
	k=nk[1]
	n=int(n)
	k=int(k)
	maxs=0
	mins=0
	if k == n :
		print("Case #"+str(kiwi+1)+": "+str(maxs)+" "+str(mins))
	else :
		for x in range(0,n):
			a.append(0)
		a.append(1)
		if n % 2 == 0 :
			a[(n//2)]=1
			b=n//2
			
		else :
			a[(n//2)+1]=1
			b=n//2+1
		
		if k == 1 :
			maxs=n-b
			mins=b-1
			print("Case #"+str(kiwi+1)+": "+str(maxs)+" "+str(mins))
		else :
			for ae in range(1,k):
				choco=comb(a)
				a[choco]=1
				if k-1==ae:
					aqwe(kiwi,choco,a)

