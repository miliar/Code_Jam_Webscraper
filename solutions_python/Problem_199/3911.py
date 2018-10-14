def Brute(state,flips,curr):
	global best
	#print(state,flips,curr,set(state))
	if best>flips and set(state)==set([True]):
		best=flips
		return
	if best<flips and best!=-1:
		return

	for next in range(curr+1, len(state)-n+1):
		tmp=state[:next]
		for k in range(next,next+n):
			tmp.append(not state[k])
		tmp+=state[next+n:]
		Brute(tmp,flips+1,next)
	return

for i in range(int(input())):
	s,n = input().split()
	n=int(n)
	tmp=[]
	for j in s:
		if j=="+":
			tmp.append(True)
		else:
			tmp.append(False)
	best=9999999999999999999999999999999999999999999999999999999999999999999999999999999
	Brute(tmp,0,-1)
	if best!=9999999999999999999999999999999999999999999999999999999999999999999999999999999:
		print("Case #"+str(i+1)+": "+str(best))
	else:
		print("Case #"+str(i+1)+": IMPOSSIBLE")