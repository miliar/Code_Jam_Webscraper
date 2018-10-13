file= open("x.txt","r")
a0=int(file.readline().rstrip())
a2=1
array=[]
for line in file:
    m=line.split()
    array.append(m)

while (a2<=a0):
    
    cookies=2.0
    time=[]
 
    b=array[a2-1]
    x=float(b[0])
    y=float(b[1])
    z=float(b[2])

    while z/cookies > (x/cookies) + (z/(cookies + y)):
        time.append(x/cookies)
        cookies+=y
    time.append(z/cookies)

    totalTime=0
    for t in time:
        totalTime+= t

    print("Case #"+str(a2)+": "+str(round(totalTime,7)))

    a2+=1
    