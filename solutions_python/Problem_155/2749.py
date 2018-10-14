a= int(raw_input())
for i in xrange(a):
    s=raw_input().split(' ')
    S=int(s[0])
    people= map(int,list(s[1]))
    sum=0
    add=0
    for j in xrange(S+1):
        if j>sum and people[j]<>0:
            add=add+j-sum
            sum=j+people[j]
        else:
            sum=sum+people[j]
    print "Case #%d: %d" %(i+1,add)

