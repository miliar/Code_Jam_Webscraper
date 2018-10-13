
import math




t = input()
f = open("out.txt","w")
filestring = ""
for i in range(t):
    li = map(int,raw_input().strip().split(' '))
    N,k = li[0],li[1]
    p = int(math.pow(2,int(math.log(k,2))))
    toilets = N - p + 1
    mins = int(toilets/p)
    maxs = mins + 1
    maxn = toilets - mins*p
    minn = p - maxn
    extras = k - p + 1
    if extras <= maxn:
        if maxs%2 != 0:
            filestring += "Case #"+str(i+1)+": "+ str(int(maxs/2)) + " " + str(int(maxs/2)) + "\n"

        else:
            filestring += "Case #"+str(i+1)+": "+str(int(maxs/2)) + " " + str(int(maxs/2)-1) +"\n"
    else:
        if mins%2 == 0:
            filestring += "Case #"+str(i+1)+": "+str(int(mins/2)) + " " + str(int(mins/2)-1) + "\n"
        else:
            filestring += "Case #"+str(i+1)+": "+str(int(mins/2)) + " " + str(int(mins/2)) + "\n"

f.write(filestring)


