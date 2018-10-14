fin=open("test.in","r")
fout=open("test.out","w")
cases=int(fin.readline())
for i in range(cases):
	n, k=map(int, fin.readline().split())
	fout.write("Case #"+str(i+1)+": "+("ON" if (k+1)%(2**n)==0 else "OFF")+"\n")
