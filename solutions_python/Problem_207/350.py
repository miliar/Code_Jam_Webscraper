t = int(input())
for tc in range(1,t+1):
	print("Case #{}: ".format(tc),end=' ')
	n,r,o,y,g,b,v = map(int,input().split())
	l = []
	l.append(('r',r))
	l.append(('y',y))
	l.append(('b',b))
	l.sort(key=lambda x:x[1])
	if (l[2][1]>l[1][1]+l[0][1]):
		print("IMPOSSIBLE")
	else:
		mx = l[2][0]
		mxval = l[2][1]
		lis = [0]*(3*l[2][1]+10)
		i = 0
		while mxval>0:
			lis[i] = mx
			i += 3
			mxval -= 1
		mx = l[1][0]
		mxval = l[1][1]
		i = 1
		while mxval>0:
			lis[i] = mx
			i += 3
			mxval -= 1
		mx = l[0][0]
		mxval = l[0][1]
		while mxval>0 and i<l[2][1]*3:
			lis[i] = mx
			i += 3
			mxval -= 1
		i = 2
		while mxval>0:
			lis[i] = mx
			mxval -= 1
			i += 3
		lis = ['' if x==0 else x for x in lis]
		print(''.join(lis))
			
