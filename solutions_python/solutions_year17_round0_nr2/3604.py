t=int(input())
case=1
while t:
    s=input()
    sss="0"*len(s)

    i=int(s)
    fin=0;
    ii=i;
    kkk=0;
    while(ii>0):
        s=str(ii);
        k=0;
        for i in range(len(s)-1):
            if(s[i]<=s[i+1]):
                k+=1
            else:
                break;
        if(k==len(s)-1):
            print("Case #"+str(case)+": "+s);
            fin=1
            break;
        else:
            if (s.count('0')==(len(s)-1-k)):
                ii-=1

            else:
                llen=(len(s)-k-1)
                ii=int(s[:k+1]+sss[:llen])

                #break;


    case+=1
    #print("Case #"+str(case)+": "+ );
    t-=1
