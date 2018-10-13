t = int(raw_input())
ans = []
for h in range(t):
    x, k = raw_input().split()
    k = int(k)
    x = ['1' if y=='+' else '0' for y in x]
    l = len(x)
    i  = 0
    count = 0
    #print l-k
    while i <= l-k:
        if x[i] == '0':
            count += 1
            for j in range(i,i+k):
                x[j] = '1' if x[j] == '0' else '0'
        i += 1

    for i in x[l-k+1:]:
        if i == '0':
            count = 'IMPOSSIBLE'
            break
    ans.append(count)

for h in range(t):
    print 'Case #'+str(h+1)+':', ans[h]
