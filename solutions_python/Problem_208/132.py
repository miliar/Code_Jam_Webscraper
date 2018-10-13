T=int(raw_input())
max_dist=[]
speed=[]
w_matrix=[]
d_matrix=[]



for t in range(T):
	s=raw_input().split(' ')
	N=int(s[0])
	Q=int(s[1])
	
	max_dist=[]
	speed=[]
	w_matrix=[]
	
	d_matrix=[]
	
	for j in range(N):
		s=raw_input().split(' ')
		max_dist+=[int(s[0])]
		speed+=[int(s[1])]
	
	for j in range(N):
		w_matrix+=[ [int(x) for x in raw_input().split(' ')] ]
	
	d_matrix=w_matrix
	
	for k in range(N):
		for i in range(N):
			for j in range(N):
				if i==j or i==k or j==k:
					continue
				
				if d_matrix[i][k]>=0 and d_matrix[k][j]>=0 and (d_matrix[i][j]<0 or d_matrix[i][j]>d_matrix[i][k]+d_matrix[k][j]):
					d_matrix[i][j]=d_matrix[i][k]+d_matrix[k][j]
	
	d2_matrix=d_matrix
	
	for i in range(N):
		for j in range(N):
			if d2_matrix[i][j]>=0 and max_dist[i]>=d2_matrix[i][j]:
					d2_matrix[i][j]=1.0*d2_matrix[i][j]/speed[i]
			else:
				d2_matrix[i][j]=-1
			
	for k in range(N):
		for i in range(N):
			for j in range(N):
				if i==j or i==k or j==k:
					continue
				
				if d2_matrix[i][k]>=0 and d_matrix[k][j]>=0 and (d_matrix[i][j]<0 or d_matrix[i][j]>d_matrix[i][k]+d_matrix[k][j]):
					d_matrix[i][j]=d_matrix[i][k]+d_matrix[k][j]
	
	l=''
	for j in range(Q):
		s=raw_input().split(' ')
		u=int(s[0])-1
		v=int(s[1])-1
		l=l+str(d2_matrix[u][v])+' '	
	print(('Case #%d: '+l) % (t+1))
		