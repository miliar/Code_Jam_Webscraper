fr = open("input3.in", "r")
fw = open("output3.txt", "w")
import math as mt
t=int(fr.readline())
#t=int(input())
for i in range(t):
    m,n=map(int,fr.readline().strip().split())
    #m,n=map(int,input().split())
    r=0
    st=mt.ceil(mt.log(n+1,2)-1)
    d=2**(st)
    a=int((m-d+1)/d)
    rem=(m-d+1)%d
    reu=n-((2**(st))-1)
    if(reu<=rem):
        r=a+1
    else:
        r=a
    #r=int((m)/(2**st))
    mx=mt.ceil((r-1)/2)
    mi2=r-mx-1
    #mi=int((m-n)/n)-1
    #l=int((m)/n)
    #ls=int(m/n)
    #print(i+1,m,n)
    #print(st,r,m,mi,mi2,mx,l,rem,reu)
    #mi=mi2
    #if(reu>(r+1)):
    #    mi+=1
    #if(mi+mx+1!=l):
    #    mi+=1
    #if(mi>mi2):
    #    mi=mi2
    #if(mi2<0):
    #    mi2=0
    #if(mi<=mx-2):
    #    mi=mx-1
    #mi=int((l-1)/2)
    #mx=mt.ceil((l-1)/2)
    #rs=
    #rs=
    #print("Case #"+str(i+1)+": "+str(mx)+" "+str(mi))
    fw.write("Case #"+str(i+1)+": "+str(mx)+" "+str(mi2)+"\n")
fw.close()
fr.close()
