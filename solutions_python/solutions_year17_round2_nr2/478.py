def seq(R, O, Y, G, B, V, s, N):
	if R<=0 and O<=0 and Y<=0 and G<=0 and B<=0 and V<=0: 
		#print "returning",s
		if len(s) == N:
			return [s]
		else:
			return []
	op = []
	if len(s)==0:
		if Y > 0:
			op += seq(R, O,Y-1,G,B,V,s+"Y",N)
		if R > 0:
			op += seq(R-1, O,Y,G,B-1,V,s+"R",N)
		if B > 0:
			op += seq(R, O,Y,G,B-1,V,s+"B",N)
			
	elif s[-1] == 'R':
		ctr = 0
		if Y > 0:
			ctr += 1
			#print s, s+"Y"
			op += seq(R, O,Y-1,G,B,V,s+"Y",N)
		if B > 0:
			ctr += 1
			op += seq(R, O,Y,G,B-1,V,s+"B",N)
		if ctr == 0 and len(s) < N:
			return []
			
	elif s[-1] == 'Y':
		ctr = 0
		if R > 0:
			ctr += 1
			op += seq(R-1, O,Y,G,B,V,s+"R",N)
		if B > 0:
			ctr += 1
			op += seq(R, O,Y,G,B-1,V,s+"B",N)
		if ctr == 0 and len(s) < N:
			return []
			
	elif s[-1] == 'B':
		ctr = 0
		if Y > 0:
			ctr += 1
			op += seq(R, O,Y-1,G,B,V,s+"Y",N)
		if R > 0:
			ctr += 1
			op += seq(R-1, O,Y,G,B-1,V,s+"R",N)
		if ctr == 0 and len(s) < N:
			return []
		
	return op

def isValid(s):
	isValid = 1
	if s[0] == s[-1]:
		return 0
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			isValid = 0
			break
	return isValid
	
t = int(raw_input())
for x in range(t):
	N, R, O, Y, G, B, V  =map(int, raw_input().split())
	#op = seq(R, O, Y, G, B, V,'',N)
	res = ''
	#R,Y,B
	
	if R >= Y and R >= B:
		if Y + B < R:
			print "Case #{}: {}".format(x+1,"IMPOSSIBLE")
			continue
		ar = ['R']*R
		ct = 0
		while B > 0 or Y > 0:
			
			if B > 0:
				ar[ct] += 'B'
				B -= 1
			elif Y > 0:
				ar[ct] += 'Y'
				Y -= 1
			ct = (ct + 1) % R
		
	elif B >= Y and B >= R:
		if Y + R < B:
			print "Case #{}: {}".format(x+1,"IMPOSSIBLE")
			continue
		ar = ['B']*B
		ct = 0
		while R > 0 or Y > 0:
			if R > 0:
				ar[ct] += 'R'
				R -= 1
			elif Y > 0:
				ar[ct] += 'Y'
				Y -= 1
			ct = (ct + 1) % B
		
	else:
		if R + B < Y:
			print "Case #{}: {}".format(x+1,"IMPOSSIBLE")
			continue
		ar = ['Y']*Y
		ct = 0	
		while R > 0 or B > 0:
			if B > 0:
				ar[ct] += 'B'
				B -= 1
			elif R > 0:
				ar[ct] += 'R'
				R -= 1
			ct = (ct + 1) % Y
	
	res = "".join(ar)
	print "Case #{}: {}".format(x+1,res)