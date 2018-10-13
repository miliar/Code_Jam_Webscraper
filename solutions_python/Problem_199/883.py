def solve():
    f=open("A-large.in")
    f2=open("output.txt",'w')
    lines=f.readlines()
    t=int(lines[0])
    # t=input()
    for test in xrange(1,t+1):
        s,k=lines[test].split()
        # s,k=raw_input().split()
        k=int(k)
        s=list(s)
        minus=s.count('-')
        ans="IMPOSSIBLE"
        if minus==0:
            ans=0
        else:
            i,count,n=0,0,len(s)
            while i<=n-k:
                while i<n and s[i]=="+":
                    i+=1
                if i<=n-k and s[i]=="-" :
                    count+=1
                    for x in xrange(k):
                        s[i+x]="+" if s[i+x]=="-" else "-"
            while i<n and s[i]=="+":
                i+=1
            if i==n:
                ans=count
        f2.write("Case #{}: {}\n".format(test,ans))
    f2.close()
    f.close()
solve()
