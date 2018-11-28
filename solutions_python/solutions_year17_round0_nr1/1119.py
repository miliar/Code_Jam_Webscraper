cases = int(input())
for case in range(1,cases+1):
    sk = input().split()
    k = int(sk[1])
    s = sk[0]
    if '-' in s:
        idx = s.index('-')
    else:
        idx = -1
    tmp = s
    count = 0
    while idx>-1 and idx+k <= len(tmp):
        flip = tmp[idx:idx+k]
        flip = flip.replace('-','*')
        flip = flip.replace('+','-')
        flip = flip.replace('*','+')
        tmp = flip + tmp[idx+k:]
        if '-' in tmp:
            idx = tmp.index('-')
        else:
            idx = -1
        count += 1
        
    if idx == -1:
        print('Case #{}: {}'.format(case, count))
    else:
        print('Case #{}: IMPOSSIBLE'.format(case))
    