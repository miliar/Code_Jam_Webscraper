fin=open("C:/codejam/2015/A/A-large.in","r")
fout=open("C:/codejam/2015/A/A-large_result.out","w")

T=int(fin.readline())

for case in range(1,T+1):
    sS_max, ss = fin.readline().rstrip('\r\n').split(' ')
    S_max=int(sS_max)
    total_up=0
    friends=0
    total_up+=int(ss[0])
    #print(ss)
    for k in range(1,len(ss)):
        #print(k)
        n=int(ss[k])
        if (n==0):
            continue
        if(k<=total_up):
            total_up+=n
        else:
            need_friends=k-total_up
            friends+=need_friends
            total_up+=n+need_friends
    fout.write("Case #"+str(case)+": "+str(friends)+"\n")
fin.close()
fout.close()
