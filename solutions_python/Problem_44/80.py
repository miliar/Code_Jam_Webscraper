f = open("B-large.in","r")
fo  = open("Bout.txt","w")
lines = f.readlines()
i = 0
#print(lines[2])
#print ( 1, sep="", file=fo)
i = 0
T = int(lines[i])
for icase in range(T):   
    i = i + 1
    N = int(lines[i])
    x =[]
    y = []
    z = []
    vx =[]
    vy = []
    vz = []
    for n in range(N):
        i = i + 1
        words = lines[i].split()
        x.append(int(words[0]))
        y.append(int(words[1]))
        z.append(int(words[2]))
        vx.append(int(words[3]))
        vy.append(int(words[4]))
        vz.append(int(words[5]))
    #print(x,vx)
    xs = sum(x)/N
    ys = sum(y)/N
    zs = sum(z)/N
    vxs = sum(vx)/N
    vys = sum(vy)/N
    vzs = sum(vz)/N
    #print(xs,vxs)
    xx = vxs*vxs+vys*vys+vzs*vzs
    print(xx,vxs,vys,vzs)
    if xx == 0:
        t = 0.0000
    else:
        t = -(vxs*xs+vys*ys+vzs*zs)/(vxs*vxs+vys*vys+vzs*vzs)
    if t < 0:
        t = 0.000000
        
    #print(t)
    #d = ((xs+vxs*t)**2+(ys+vys*t)(ys+vys*t)+(zs+vzs*t)(zs+vzs*t))
    d = (xs+vxs*t)**2+(ys+vys*t)**2+(zs+vzs*t)**2
    d = d**0.5
    print("Case #",icase+1,": ",d," ",t,sep="")
    print("Case #",icase+1,": ",d," ",t,sep="",file=fo)
f.close()
fo.close()








