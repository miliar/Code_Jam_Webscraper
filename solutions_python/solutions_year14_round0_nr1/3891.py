read_file = open('A-small-attempt0.in', 'r')
write_file = open('writefile.txt', 'w')
t=int(read_file.readline())
trace=t
while(t!=0):
    t=t-1
    ans1=int(read_file.readline())
    sq1=[]
    sq2=[]
    k=[]
    for j in range (0,4):
        k=read_file.readline().split(' ')
        for i in range(0,4):
            k[i]=int(k[i])
        sq1.append(k)
    ans2=int(read_file.readline())
    k=[]
    for j in range (0,4):
        k=read_file.readline().split(' ')
        for i in range(0,4):
            k[i]=int(k[i])
        sq2.append(k)
    match=0
    no=0
    for i in range(0,4):
        for j in range(0,4):
            if sq1[ans1-1][i]==sq2[ans2-1][j]:
                match = match+1
                no=sq1[ans1-1][i]
    if match==1:
        print("Case #"+str(trace-t)+": "+str(no))
    elif match>1:
        print("Case #"+str(trace-t)+": Bad magician!")
    else:
        print("Case #"+str(trace-t)+": Volunteer cheated!")
