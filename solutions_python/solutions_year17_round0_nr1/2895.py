clo = open("output.txt", 'w')
with open("input.txt") as f:
    t = int(f.readline())
    for i in range(t):
        s ,k = map(str,f.readline().strip().split(' '))
        k = int(k)
        l=len(s)
        flips=0
        if k <= l:
            for j in range(l-k+1):
                if s[j] == '-':
                    ans=''
                    for m in range(k):
                        if s[j+m] == '-':
                            ans+='+'
                        else:
                            ans+='-'
                    s=s[:j]+ans+s[j+k:]
                    flips+=1
        if i!=0:
            clo.write('\n')
        if '-' in s:
            clo.write("Case #"+str(i+1)+": IMPOSSIBLE")
        else:
            clo.write("Case #"+str(i+1)+": "+str(flips))