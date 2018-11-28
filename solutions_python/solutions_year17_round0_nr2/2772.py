#!/usr/bin/python
t = int(input())
for i in range(1, t + 1):
        n = list(raw_input())
	lastd=9
        for j in range(len(n)-1,-1,-1):
		if int(n[j])>lastd:
			for k in range(j+1,len(n)):
				n[k]='9'
			n[j]=str(int(n[j])-1)
		lastd=int(n[j])
        print("Case #{}: {}".format(i,int("".join(n))))
