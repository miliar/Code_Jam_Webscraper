t = int(raw_input())
for i in range(1,t+1):
    cool_scores = 0
    surprising_scores = 0
    line = raw_input().split()
    n = int(line[0])
    s = int(line[1])
    p = int(line[2])
    for j in range(3,n+3):
        k = int(line[j])
        if k >= max(3*p-2,p):
            cool_scores+=1
        elif k >= max(3*p-4,p):
            surprising_scores+=1
    print 'Case #{}: {}'.format(i,cool_scores+min(surprising_scores,s))
