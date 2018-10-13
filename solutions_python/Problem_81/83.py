import sys

T = int(sys.stdin.readline().strip())
for t in range(1,T+1):
	N=int(sys.stdin.readline().strip())
	S=[]
	
	for i in range(N):
		s=sys.stdin.readline().strip()
		S.append(s)
	
	WP  = []
	OWP = []
	OOWP = []
	
	for i in range(N):
		w,l=0,0
		for j in range(N):
			if S[i][j]=='.':continue
			if S[i][j]=='0': l+=1
			else: w+=1
		WP.append((w*1.0,l))
	
	for i in range(N):
		owp=[]
		for j in range(N):
			if S[i][j]=='.':continue
			if S[i][j]=='1': 
				owp.append(WP[j][0]/(WP[j][0]+WP[j][1]-1))
			else: 
				owp.append((WP[j][0]-1)/(WP[j][0]+WP[j][1]-1))
		OWP.append(sum(owp)/len(owp))
	
	for i in range(N):
		oowp=[]
		for j in range(N):
			if S[i][j]=='.':continue
			oowp.append(OWP[j])
		OOWP.append(sum(oowp)/len(oowp))
	
	print 'Case #%d:' % t
	
	for i in range(N):
		wp = WP[i][0]/(WP[i][0]+WP[i][1])
		#print wp, OWP[i], OOWP[i]
		print (.25*(WP[i][0]/(WP[i][0]+WP[i][1]))+.50*OWP[i]+.25*OOWP[i])
