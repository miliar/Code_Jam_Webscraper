import sys
#sys.stdin = open('input.in','r')
#sys.stdout = open('output.in','w')
t=int(input())
test = 0
while test<t:
    test+=1
    n=list(input())
    if(len(n)!=1):
        i=1
        ln = len(n)
        f = False
        while(i<ln):
            if(ord(n[i-1])>ord(n[i])):
                n[i]='9'
                j=i-1
                if(f==False):
                    n[j]=chr(ord(n[j])-1)
                    f=True
                    while(j>0 and ord(n[j])<ord(n[j-1])):
                        n[j]='9'
                        n[j-1]=chr(ord(n[j-1])-1)
                        j-=1
            i+=1
    tot = ""
    for i in n:
        tot+=i
    print("Case #"+str(test)+": "+str(int(tot)))