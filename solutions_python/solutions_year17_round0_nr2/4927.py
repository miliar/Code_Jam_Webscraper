'''

   SANJAY GIDWANI (sgidwani96)
          -> programmer & developer

'''

# import adorkable
import sys

t=input()
i=0
while(i<t):
    n=input()
    for j in range(1,n+1):
        count=0
        st=str(j)
        for k in range(0,len(st)-1):
            if(st[k]<=st[k+1]):
                count+=1
            else:
                break
        if(count==len(st)-1):
            tidy=st
        
    sys.stdout.write('Case #')
    sys.stdout.write(str(i+1))
    sys.stdout.write(': ')
    sys.stdout.write(tidy)
    print
    i+=1
