fin="/home/aksh/Downloads/A-large.in"
fout="Alargeout.txt"
file = open(fin, "r")
t=int(file.readline())


ans=[]
for i in range(t):
    d,n = map(int,file.readline().strip().split(' '))
    
    distarr = []
    speedmap = {}
    for j in range(n):
        x,y = map(float,file.readline().strip().split(' '))
        distarr.append(x)
        speedmap[x] = y

    arr = sorted(distarr, key=int, reverse=True)


    timep = (d - arr[0])/speedmap[arr[0]]

    for j in range(1,n):
        time = (d - arr[j])/speedmap[arr[j]]

        if time > timep:
            timep=time
        

    speed = d/timep


    


    ans.append('{0:.6f}'.format(speed))
            
        
print ans

file.close()
file = open(fout, "w")

for i in range(t):
    file.write("Case #"+str(i+1)+": "+ans[i]+'\n')
file.close()

