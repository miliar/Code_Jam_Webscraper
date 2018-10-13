t=int(input())
for i in range(t):
    line=input().split(' ')
    s=line[0]
    k=int(line[1])
    l=len(s)
    j=s.find('-')
    count=0
    while(j<=l-k and j!=-1):
        count+=1
        for m in range(j,j+k):
            if(s[m]=='-'):
                s=s[:m]+'+'+s[m+1:]
            else:
                s=s[:m]+'-'+s[m+1:]
        j=s.find('-')
    
    if('-' in s):
        print ("Case #{}: {}".format(i+1,"IMPOSSIBLE"))
    else:
        print ("Case #{}: {}".format(i+1,count))
        
    
