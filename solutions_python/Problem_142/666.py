from sys import stdin as cin,stdout as cout
from collections import Counter
from itertools import groupby
for t in range( int(cin.readline())):
	n = int(cin.readline())
	a= cin.readline()
	b= cin.readline()
	count = 0
	c  = [[k,len(list(g))] for k, g in groupby(a)]
	d = [[k,len(list(g))] for k, g in groupby(b)]
	flag = 1
	j=0
	for x in c:
		if x[0] == d[j][0]:
			count+=abs(x[1]-d[j][1])
			j+=1
		else:
			flag = 0
			break


	if flag==0:
		cout.write('Case #'+str(t+1)+': Fegla Won\n')
	else:
		cout.write('Case #'+str(t+1)+': '+str(count)+'\n')




