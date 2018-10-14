tcs = int(raw_input())
for t in range(1,tcs+1):
    data = raw_input().split()
    seq = list(data[0])
    k = int(data[1])
    l = len(seq)
    answer = 0
    while l>=k:
        if seq[l-1]=='-':
            answer+=1
            j = l-1
            for i in range(0, k):
                if seq[j]=='+':
                    seq[j] = '-'
                else: 
                    seq[j] = '+'
                j-=1
        l-=1
    while l>=1:
        if seq[l-1]=='-':
            answer=-1
            break
        l-=1
    if answer==-1:
        answer='IMPOSSIBLE'
    print 'Case #{}: {}'.format(t, answer)
