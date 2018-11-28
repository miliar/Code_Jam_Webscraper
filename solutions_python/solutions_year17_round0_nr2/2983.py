import sys
sys.stdout=open("output.txt","w")
for tc in range(int(raw_input())):
    no=raw_input()
    lst=list(no)
    for i in range(len(lst)-1,0,-1):
        if int(lst[i])<int(lst[i-1]):
            lst[i-1]=str(int(lst[i-1])-1)
            for j in range(i,len(lst)):
                lst[j]='9'
    flag=True
    s=""
    for j in range(len(lst)):
        if not (flag and lst[j]=='0'):
            flag=False
            s+=lst[j]
    print 'Case #'+str(tc+1)+': '+s
sys.stdout.close()