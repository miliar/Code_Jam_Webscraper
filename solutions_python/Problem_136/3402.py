f=open('B-small-attempt0 (1).in','r')

x=int(f.readline()[:-1])

def countSum(C,noFarm,F):
    x=0.0
    for i in range(noFarm+1):
       x+=C/(2+i*F)
    return x

for i in range(x):
    a=f.readline()[:-1].split()
    C=float(a[0])
    F=float(a[1])
    X=float(a[2])
    noFarm=0
    while countSum(C,noFarm-1,F) + X/(2+noFarm*F) > countSum(C,noFarm,F) + X/(2+(noFarm+1)*F):
        noFarm+=1
    time = countSum(C,noFarm-1,F) + X/(2+(noFarm)*F)
    print('Case #' + str(i+1) + ': ' + str(time))
    
        

