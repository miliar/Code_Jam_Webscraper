ans = None
def getmax( gap,k, track):
	global ans;
	l=max(track);
	rem = l
	if(l%2 == 0 ):
		cnt = gap[l];
		
		l=int(l/2);
		if(cnt >= k):
			ans = (l,l-1)
			return 0;
		else:
			if(l not in gap):
				gap[l] = cnt
				track.add(l)
			else:
				gap[l] = gap[l]+cnt
			
			if(l-1 not in gap):
				gap[l-1] = cnt
				track.add(l-1)
			else:
				gap[l-1] = gap[l-1]+cnt
				
			track.remove(rem);
			#gap.pop(rem, None)
			return k-cnt
	else:
		cnt = gap[l];
		l=int(l/2)+1;
		if(cnt >= k):
			ans = (l-1,l-1)
			return 0;
		else:
			if(l-1 not in gap):
				gap[l-1]=cnt*2;
				track.add(l-1)
			else:
				gap[l-1] = gap[l-1] + 2*cnt;
			
			track.remove(rem);
			#gap.pop(rem, None)
			return k-cnt;
			
		
		
		
	#g=max(gap)
	#l=g
	#gap.remove(g);
	#if(l%2==0):
		#l=int(l/2);
		#gap.append(l)
		#gap.append(l-1)
		#return (l,l-1)
	#else:
		#l=int(l/2)+1;
		#gap.append(l-1)
		#gap.append(l-1)
		#return (l-1,l-1)
	
		
	
	
x = int(input())
for v in range(x):
	n,k = map(int,input().split(" "))
	#a = [0 for i in range(n+1)]
	ans=None
	gap={n:1};
	track = set([n]);
	while(k != 0):
		k=getmax(gap,k,track)
		
	#for i in range(k):
		#ans=getmax(n,k,gap,a)
	#print(gap)
		
		
	print("Case #"+str(v+1)+":",max(ans),min(ans))
