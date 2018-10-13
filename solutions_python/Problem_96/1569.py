a = open('B-large.in','r')
b = open('answer-large.txt','w')
maxdiff = 2
case = 0

for line in a:
    case+=1
    c = []
    cnt = 0
    c = map(int,line.split())
    googlers = c[0]+3
    surprise = c[1]
    max = c[2]
    for i in range(3,googlers):
        if c[i]==0 and max!=0:
            continue
        remainder = c[i]%3
        average = c[i]/3
        if average>=max:
            cnt+=1
        elif average<max and remainder==1:
            newhigh = average+remainder
            if newhigh>=max:
                cnt+=1
        elif average<max and remainder==2:
            newhigh = average+1
            if newhigh>=max:
                cnt+=1
            else:
                newhigh = average+remainder
                if newhigh>=max and surprise!=0:
                    cnt+=1
                    surprise-=1
        elif average<max and remainder==0:
            newhigh = average+1
            if newhigh>=max and surprise!=0:
                cnt+=1
                surprise-=1
    b.write("Case #"+str(case)+": "+str(cnt)+"\n")
a.close()
b.close()
