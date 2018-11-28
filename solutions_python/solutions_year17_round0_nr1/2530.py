

def check(s,k,count,x) :
    for j in range(0,len(s)) :
		if j+k <= len(s) and s[j] == '-' :
			count += 1
			for i in range(j,j+k) :
				if s[i] == '-' :
					s[i] = '+'
				elif s[i] == '+' :
					s[i] = '-'
                elif j+k > len(s) :
	           for i in range(j,len(s)) :
			if s[i] == '-' :
			     return ('Case #'+str(x)+': '+'IMPOSSIBLE')
    return ('Case #'+str(x)+': '+str(count))
t=int(raw_input())
x=0
mylist=[];
while t>0 :
        x += 1
        t = t-1
        
        s=[];
	s,k = map(str,raw_input().split())
        #print s
        s=list(s)
        #print s
        k=int(k)
	count=0
	mylist.append(check(s,k,count,x))
        #print mylist
for p in mylist :
     print p
