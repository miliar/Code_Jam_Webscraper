def check_row(S,K):
	L = len(S)
	S = np.array([1 if s=='+' else 0 for s in list(S)])

	score_p = -1
	S_p = np.zeros_like(S)+2
	S_p_p = np.zeros_like(S)+2
	rounds = 0
	locs = np.where(S==0)[0]
	if len(locs)==0:
		return True,0
	pos_1 = locs[0]
	pos_2 = L-locs[-1]-1
	score = min(pos_1,pos_2)
	#print S,pos_1,pos_2,score,rounds,np.sum(S),L
	while score>=score_p and np.sum(S==S_p)!=L and np.sum(S==S_p_p)!=L:
		if np.sum(S)==L:
			return True,rounds
		S_p_p=S_p.copy()
		S_p=S.copy()
		score_p=score
		if pos_1<=pos_2:
			if pos_1+K<=L:
				S[pos_1:pos_1+K] = (S[pos_1:pos_1+K]==0).astype(np.int)
		else:
			if pos_2+K<=L:
				S[L-pos_2-K:L-pos_2] = (S[L-pos_2-K:L-pos_2]==0).astype(np.int)
		rounds+=1
		locs = np.where(S==0)[0]
		if len(locs)>0:
			pos_1 = locs[0]
			pos_2 = L-locs[-1]-1
			score = min(pos_1,pos_2)
			#print S,pos_1,pos_2,score,rounds,np.sum(S),L
		else:
			#print S,pos_1,pos_2,score,rounds,np.sum(S),L
			return True,rounds
	if np.sum(S)==L:
		return True,rounds
	else:
		#print score,score_p,np.sum(S==S_p),L,S,S_p
		return False,rounds

out_lines = []
with open('../A-large.in') as f:
	for i,line in enumerate(f):
		if i>0:
			S,K=line.split()
			K=int(K)
			good,rounds = check_row(S,K)
			if good:
				out_lines.append('Case #'+str(i)+': '+str(rounds)+'\n')
			else:
				out_lines.append('Case #'+str(i)+': IMPOSSIBLE\n')

#print out_lines

with open('A-large.out','w') as f:
	for line in out_lines:
		f.write(line)

