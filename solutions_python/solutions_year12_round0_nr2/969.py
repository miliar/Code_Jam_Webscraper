#python32
#coding = utf-8

def cal(a,n):
	if n == 0 :
		return [1,0]
	elif n == 1 :
		if a>0:
			return [1,0]
		else:
			return [0,0]
	elif (n-2)*2+n-1>=a:
		return [0,0]
	elif (n-2)*2+n == a:
		return [0,1]
	elif n-2+n-1+n == a:
		return [0,1]
	else:
		return [1,1]
		

def cal_all(b,n,x):
	ans = []
	c = 0
	for i in b:
		#print(cal(i,n))
		ans.append(cal(i,n))
	for j in ans:
		if j[0]:
			c = c+1
		elif j[0]==0 and x>0 and j[1]:
			c = c+1
			x = x-1
	return c
	
file0 = open("B-large.in",'r')
file1 = open("bout","w")
num = int(file0.readline())


for i in range(num):
	vs = file0.readline().split("\n")[0].split(" ")
	for j in range(len(vs)):
		vs[j] = int(vs[j])
	file1.write("Case #"+str(i+1)+": "+str(cal_all(vs[3:],vs[2],vs[1]))+'\n')
