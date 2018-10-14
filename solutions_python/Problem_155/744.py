
f = open("input.in","r")
fout = open("output.out","w")
tt = int(f.readline())
case = 0
while tt>0:
	tt-=1
	n,a = f.readline().split(' ')
	n = int(n)
	a = map(int,list(a)[0:-1])
	now = 0
	need = 0
	ans = 0
	for i in a:
		if now < need:
			ans += need-now
			now = need
		now += i
		need+=1
	case+=1
	fout.write("Case #"+str(case)+": "+str(ans)+"\n")
	



