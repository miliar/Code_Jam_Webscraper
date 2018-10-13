T=input()
for q in range(1,T+1):
 n=input()
 arr2=[float(x) for x in raw_input().split()]
 arr1=[float(x) for x in raw_input().split()]
 arr1.sort()
 arr2.sort()
 i=n-1
 count=0
 j=n-1
 while((i>=0)&(j>=0)):
     if(arr2[i]>arr1[j]):
        count+=1
     else:
         j-=1
     i-=1
 i=n-1
 count2=0
 j=n-1
 while((i>=0)&(j>=0)):
     if(arr2[i]>arr1[j]):
        count2+=1
        arr1=arr1[:j]
        arr2=arr2[:i]
     else:
         arr1=arr1[:j]
         arr2=arr2[1:]
     j-=1
     i-=1    
 print "Case #"+str(q)+": "+str(count2)+" "+str(count)       
