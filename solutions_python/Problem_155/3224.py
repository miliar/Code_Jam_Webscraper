f = open('A-large.in','r')

T = int(f.readline())

ans = []
0040201
for i in range(0,T):
	a = f.readline().split()
	added = 0
	summ = 0
	for j in range(0,len(a[1])):
		if a[1][j]!='0' and summ<j:
				while j<summ:
					summ+=1
					added+=1
		elif a[1][j]!='0':
				summ=summ+int(a[1][j])
		elif a[1][j]=='0' and j==summ:
			summ+=1
			added+=1
	ans.append(added)
fw = open('output.in','w')
for i in range(0,T):
	fw.write('Case #'+str(i+1)+': '+str(ans[i])+'\n')
fw.close()