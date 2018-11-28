#fi=open("C:\\users\\Sergiy\\Downloads\\A-small-attempt0 (1).in",'r')
#fo=open("C:\\users\\Sergiy\\Downloads\\A-small-attempt0.out",'w')
fi=open("C:\users\Sergiy\Downloads\A-large.in",r)
fo=open("C:\users\Sergiy\Downloads\A-large.out",w)

def calc():
    ans=0    
    s,k=fi.readline().split()
    s=[1 if x=='+' else 0 for x in s]
    k=int(k)
    for i in range(len(s)-k+1):
        if not s[i]: 
            s[i:i+k]=[1-x for x in s[i:i+k]]
            ans+=1
    return "IMPOSSIBLE" if sum(s)!=len(s) else ans
        
for testNo in range(int(fi.readline())): print("Case #{}: {}".format(testNo+1,calc()),file=fo)

fo.close()
print("Ok")