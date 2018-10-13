t=input()
string=[]
for i in range(int(t)):
    count=0
    flag=0
    string=input()
    string,k=string.split(" ")
    string=list(string)
    
    for j in range(len(string)-(int(k))+1):
        if string[j]=='-':
            count+=1
            for n in range(int(k)):
                if string[n+j]=='-':
                    string[n+j]='+'
                else:
                    string[n+j]='-'


    for j in range(len(string)):
        if string[j]=='-':
            flag=1

    if flag==1:
        print("Case #{0}: IMPOSSIBLE".format(i+1))
    else:
        print("Case #{0}: ".format(i+1)+ str(count))
    
