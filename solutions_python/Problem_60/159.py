import sys
inputFile=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\b-small.in')
output=open(r'C:\Documents and Settings\shastri\Desktop\CODEJAM 2010\1B\b-small.out',mode='w')
sys.stdin = inputFile
c = int(input())
for i in range(1,c+1):
    n,k,b,t =[int(l) for l in input().split()]
    x=[int(l) for l in input().split()]
    v=[int(l) for l in input().split()]
    v=[v[l]*t+x[l] for l in range(n)]
    ans=0
    #print('Case  ',i,' ',n,k,b,t)
    #print(v)
    for l in range(n-1,n-k-1,-1):
        
        if(v[l]<b):
            j=l            
                        
            while v[j]<b and j>0:                                
                j-=1
                ans+=1
            temp=v[j]
            while j<l:
                v[j] = v[j+1]
                j+=1
            v[l]=temp
    #print(v)    
    for l in range(n-1,n-k-1,-1):
        #print(l)
        if(v[l]<b):
            ans='IMPOSSIBLE'
    #print(ans)
    print('Case #{0}: {1}'.format(i,ans),file=output)
output.close()
inputFile.close()
