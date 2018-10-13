from itertools import combinations
import math
def area(list):
	ar = math.pi*list[0][0]**2
	ar += 2*math.pi*list[0][0]*list[0][1]
	for i in range(1,len(list)):
		ar += 2*math.pi*list[i][0]*list[i][1]
		ar += math.pi*(list[i][0]**2-list[i-1][0]**2)
	return ar

def calc(list,n,k):
	list.sort()
	maxar = -1
	#print list
	for i in combinations(list,k):
		maxar = max(maxar,area(i))
		#print i,area(i)
	return maxar
	


f = open("test.txt")
#f2 = open("out.txt","w")
t = int(f.readline())

for i in range(1,t+1):
	x = (f.readline())
	x = x.split()
	#print(x)
	d = int(x[0])
	n = int(x[1])
	list = []
	#print(d,n)
	for j in range(0,d):
		y = (f.readline())
		y = y.split()
		list.append([int(y[0]),int(y[1])])
	ans = calc(list,d,n)
	print("Case #"+str(i)+": "+'{0:.16f}'.format(ans))
	
