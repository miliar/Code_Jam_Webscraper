f = open("A-large.in","r")
out = open("output1.out","a")
case = int(f.readline())
def flip(x):
    for i in range(len(x)):
        if x[i]=='+':
            x[i]='-'
        else:
            x[i]='+'
    return list(x)
o=[]
def chk(x):
	for i in x:
		if i=='-':
			return 1
	return 0
k=0
for i in range(case):
    inp = f.readline().split(" ")
    c,n=0,0
    k= int(inp.pop())
    inp = list(inp[0])
    for j in range(len(inp)):
        if inp[j] == '-':
            if (k+j)>len(inp) and chk(inp):
                o.append("IMPOSSIBLE")
                c+=1
                break
            inp[j:j+k]=flip(inp[j:j+k])
            n+=1
    if c != 1:
        o.append(n)
for i in range(case):
	out.write("Case #"+str(i+1)+": "+str(o[i])+"\n")
out.close()
f.close()
