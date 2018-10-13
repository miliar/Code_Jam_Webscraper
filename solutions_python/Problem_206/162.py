#originally thought the other horses have a destination, so they can "disappear" in the middle of the road
#would've made the task a lot more interesting, but apparently this one is easy
for L in range(int(input())):
	(dest,numhorses) = [t(s) for t,s in zip((int,int),input().split())]
	others = [[t(s) for t,s in zip((int,int),input().split())] for _ in range(numhorses)]
	
	time = max([(dest-pos)/spd for pos,spd in others])
	
	print("Case #"+str(L+1)+":", dest/time)
