f = open('output.txt','w')
t = int(raw_input())
for l in range(0, t):
    m, n, o = map(int, raw_input().split())
    count = 0
    for i in range(0, m):
	for j in range(0, n):
	    if (i&j)<o:
		count=count+1
    st = "Case #"+str((l+1))+": "+str(count)
    print st
    f.write(st+"\n")
f.close()
