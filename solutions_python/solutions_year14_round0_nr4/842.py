import copy
def main():
    a=open("D-large.in","r")
    b=open("Answer_D(5).out","w")
    q=a.readline()
    #q=input()
    q=int(q)
    u=1
    while(q>0):
        count=0
        ans=0
        no=int(a.readline())
        lst=map(float,a.readline().split())
        lst.sort()
        lst2=map(float,a.readline().split())
        lst2.sort()
        lst3=copy.copy(lst2)
        #print lst
        #print lst2
        for i in lst:
            if i < lst2[0]:
                count=count+1
        j=0
        i=count
        lst2=lst2[:no-count]
        x=no-count
        ans=0
        #---------------------------------------------
        #print count
        while x>=0 and i<=no-1:
            #print ans,x,i
            #print count
            if lst[i] > lst2[j]:
                ans=ans+1
                i=i+1
                j=j+1
            else:
                x = x-1
                lst2=lst2[:x]
                i=i+1
        b.write("Case #"+str(u)+": "+str(ans)),
        #---optimally--------------------------------------------
        ans=no
        cnt=0
        #print lst
        #print lst3
        for i in lst:
            #print cnt
            lst3=lst3[cnt:]
            cnt=0
            for j in lst3:
                cnt=cnt+1
                if j>i:
                    ans=ans-1
                    break
        b.write(" "+str(ans)+'\n')
            
        u=u+1
        q=q-1

if __name__ == "__main__":
    main()
