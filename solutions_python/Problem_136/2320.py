file = open('B-large.in')
lines=file.readlines()
fileout=open('B-large.out','w')
r=2
time=0.00
for x in range(1,len(lines)):
    set1=lines[x].split()
    c=float(set1[0])
    f=float(set1[1])
    z=float(set1[2])
    while z/r > (c/(r))+ (z/(r+f)):
        time=time+(c/r)
        r=r+f
    time=time+(z/r)
    print('Case #'+str(x)+': '+str(time))
    fileout.write('Case #'+str(x)+': '+str(time)+'\n')
    time=0.00
    r=2

file.close()
fileout.close()
        

