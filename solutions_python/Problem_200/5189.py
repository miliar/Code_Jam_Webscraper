def small(k):
    for i in range(1,len(k)):
        if int(k[i])<int(k[i-1]):
            return False
    return True
inp=open("input.txt","r")
t=inp.readline()
t=int(t)
f=open("output.txt","w")
for l in range(t):
    n=inp.readline()
    n=int(n)
    for i in range(n,0,-1):
        if small(str(i)):
            f.write("Case #"+str(l+1)+": "+str(i))
            f.write("\n")
            break
f.close()
inp.close()