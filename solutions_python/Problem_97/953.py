#python32
#coding = utf-8

def cal0(a,x,y):
	ans = []
	for i in range(len(a)):
		b = int(''.join(a[i:])+''.join(a[:i]));
		if b>=x and b<=y:
			ans.append(b)
	return list(set(ans))

def cal(a,b):
	rec = []
	ans = 0
	for i in range(a,b+1):
		if i not in rec:
			ns = list(str(i))
			t1 = cal0(ns,a,b)
			rec.extend(t1)	
			ans = ans+(len(t1)-1)*len(t1)/2
	#print(rec)
	return int(ans)


file0 = open("C-small-attempt0.in",'r')
file1 = open("cout",'w')

num = int(file0.readline())

for i in range(num):
	vs = file0.readline().split("\n")[0].split(" ")
	file1.write("Case #"+str(i+1)+": "+str(cal(int(vs[0]),int(vs[1])))+"\n")
	
