from bisect import *
def naomicheat(f="E:\\Users\\Neta\\Downloads\\D-large.in"):
    file = open(f, 'r')
    iternumber=int(file.readline().replace("\n",""))
    for k in range(iternumber):
        n=int(file.readline().replace("\n",""))
        naomi=sorted(file.readline().replace("\n","").split(" "))
        ken=sorted(file.readline().replace("\n","").split(" "))
        naomi=[float(i) for i in naomi]
        ken=[float(i) for i in ken]
        i=0
        j=0
        cheat=0
        legal=0
        #Stable solution provided, it's 3 and a half at the morning and im still
        #at this thingy... too tired to solve the 3rd question
        #at this point, i didn't even consider if this solutin is better
        #than the previous one, but Baylife.
        while(i<n):
            if(ken[j]>naomi[i]):
                i=find_lt(naomi[i:],ken[j])+i+1
            else:
                j=j+1
                i=i+1
                cheat=cheat+1
        i=n-1
        j=n-1
        while(i>=0):
            if(ken[j]<naomi[i]):
                i=i-1
                legal=legal+1
            else:
                j=j-1
                i=i-1
        print("Case #"+str(k+1)+": "+str(cheat)+" "+str(legal))
                
def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return i-1
    raise ValueError
