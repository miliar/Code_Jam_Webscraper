f1 = open("A-large.in","r")
f2 = open("out.txt","w")

data = f1.readlines()
k = int((data[0].split())[0])
ind=1
for i in range(k):
    dim=data[ind].split()
    ind+=1
    d = float(dim[0])
    n = int(dim[1])
    k = 0.0
    s = 0.0
    t = 0.0
    for j in range(n):
        line = data[ind].split()
        k=float(line[0])
        s=float(line[1])
        t=(d-k)/s
        ind+=1
        ms = s + k/t
        if j>=1:
            minspeed = min(minspeed, ms)
        else:
            minspeed = ms
    f2.write("Case #"+str(i+1)+": "+str("{:.6f}".format(minspeed))+"\n")

f1.close()
f2.close()
