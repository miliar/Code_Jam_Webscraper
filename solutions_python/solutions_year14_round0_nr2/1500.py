def cookies(f="E:\\Users\\Neta\\Downloads\\B-large.in"):
    file = open(f, 'r')
    iternumber=int(file.readline().replace("\n",""))
    for i in range(iternumber):
        costs=file.readline().replace("\n","").split(" ")
        c=float(costs[0])
        f=float(costs[1])
        x=float(costs[2])
        p=int((x/c)-(2/f))
        som=0
        for j in range (p):
            som=som+1/(2+(f*j))
        som=som*c
        if(p>0):
            som=som+x/(2+(p*f))
        else:
            som=(x/2)
        print("Case #"+str(i+1)+": "+str(som))
