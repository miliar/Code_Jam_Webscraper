t = int(input())
ret = []
for l in range(t):
    line = input().split()
    s,k = line[0], int(line[1])
    s = list(s)
    total = 0
    for i in range(len(s)):
        if s[i] == '-' and i<=len(s)-k:
            total += 1
            for j in range(i,i+k): s[j] = '+' if s[j]=='-' else '-'
    possible = True
    for x in s: 
        if x=='-':
            possible = False
            break
    if not possible: total = -1
    ret.append(total)

for i in range(len(ret)):
    print('Case #%d: %s'%(i+1, str(ret[i]) if ret[i]!= -1 else 'IMPOSSIBLE' ))
