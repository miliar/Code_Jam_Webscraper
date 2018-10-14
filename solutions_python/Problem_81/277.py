# python 3
T=int(input())
for t in range(1,T+1):
	print("Case #%d:"%t)
	N=int(input())
	sb=[]
	wp=[]
	owp=[]
	#oowp=[]
	for i in range(N):
		sb.append(input())
	for i in range(N):
		nbm=0
		tot=0
		for j in sb[i]:
			if j=='.': continue
			nbm+=1
			if j=='1': tot+=1
		wp.append((tot,nbm))
		
	for i in range(len(sb)):
		owptot=0
		nbowp=0
		for j in range(len(sb[i])):
			if sb[i][j]=='.':continue
			(totwp,nbwp)=wp[j]
			owptot+=(totwp-int(sb[j][i]))/(nbwp-1)
			nbowp+=1
		owp.append(owptot/nbowp)
		
	for i in range(N):
		tot=0
		nb=0
		for j in range(len(sb[i])):
			if sb[i][j]=='.':continue
			tot+=owp[j]
			nb+=1
		#oowp.append(tot/nb)
		#print("i------------->",i)
		#print("wp",wp[i])
		#print("owp",owp[i])
		#print("oowp",tot,nb)
		(totwp,nbwp)=wp[i]
		print(0.25*totwp/nbwp + 0.5*owp[i] + 0.25*tot/nb)