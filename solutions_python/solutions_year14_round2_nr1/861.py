import math
tc = input()
counter = 1
fo = open("out","w")
while counter<=tc:
	ans="Fegla Won"
	N = input()
	S=[]
	S.append(raw_input())
	chars=[]
	charcounthorizontal=[]
	feglawon = 0
	ll=[]
	for jk in xrange(len(S[0])):
			char=S[0][jk]
			if jk==0:
				chars.append(S[0][0])
				ll.append(1)
			else:
				if chars[-1]==char:
					ll[-1]= ll[-1]+1
				else:
					chars.append(char)
					ll.append(1)
	charcounthorizontal.append(list(ll))
	print chars
	print charcounthorizontal
	for x in xrange(1,N):
		S.append(raw_input())
		l=[]
		ll=[]
		for jk in xrange(len(S[x])):
			char=S[x][jk]
			if jk==0:
				l.append(S[x][0])
				ll.append(1)
			else:
				if l[-1]==char:
					ll[-1]= ll[-1]+1
				else:
					l.append(char)
					ll.append(1)
		if chars!=l:
			feglawon=1
			break
		else:
			charcounthorizontal.append(list(ll))
	if feglawon==0:
		ans=0
		for nc in xrange(len(chars)):
			charcount=[]
			for i in xrange(N):
				charcount.append(charcounthorizontal[i][nc])
			charcount.sort()
			# print charcount
			if N%2==1:
				q=charcount[N/2]
			else:
				q=int(math.floor((charcount[N/2]+charcount[N/2-1])/2.0+0.5))
			for cc in charcount:
				ans = ans + abs(cc-q)
	# print "Case #"+str(counter)+": "+str(ans)
	fo.write("Case #"+str(counter)+": "+str(ans)+"\n")
	counter=counter+1
fo.close()
	