Cases = int(input())
for Case in range(Cases):
    k = int(input())
    d = list(map(int,list(str(k))))
    for q in range(len(d)):
        for i in range(len(d)-1):
            if d[i+1] < d[i]:
                d[i] -= 1
                for j in range(i+1,len(d)):
                    d[j] = 9
                break
    ans = int(''.join(map(str,d)))
    print('Case #%d: %d' % (Case+1, ans))