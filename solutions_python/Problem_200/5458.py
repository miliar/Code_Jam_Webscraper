def tidyn(N,d):
	cnt = 0
	for i in range(0,d-1):
		if N[i] > N[i+1]:
			if cnt > 0:
				N[0]= N[0]-1
				for j in range(0,cnt+1):
					N[j+1] = 9
				cnt = 0

			else:  
				N[i] = N[i]-1
				for j in range(i+1,d):
					N[j] = 9

			n = 0
			for i in range(0,d):
				n = n+10**(i)*N[d-i-1]
			return n

		elif N[i]==N[i+1]:
			cnt = cnt+1






f = open('B-small-attempt6.in','r')
l = []
for line in f: 
	l.append(line)

leng = l[0]
l.pop(0)

for i in range(0,len(l)):
	l[i] = int(l[i])


j = 0
lst = [-1 for i in range(0,len(l))]
for N in l:
	d = len(str(N))
	n = [-1 for i in range(0,d)]
	#print(N,d)
	for i in range(0,d):
		#print(int(N/10**(d-1-i) %10))
		n[i] = int(N/10**(d-1-i) %10)

	#print(N,'--> ', n)

	lst[j] = tidyn(n,d)
	lst[j] = str(lst[j])
	j = j+1


#print('99999999999999999')
#print(tidyn([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],len(str(111111111111111110))))

for i in range(0,len(l)):
	if lst[i] ==  'None':
		lst[i] = l[i]

	print(l[i],': ',lst[i])

tar = open('ans.txt','w')
tar.truncate()

for i in range(0,len(lst)):

	tar.write('Case #'+str(i+1)+': '+str(lst[i]))
	tar.write("\n")

tar.close()

