def next_p(k):
    l_s = (k-1)//2
    r_s = k - l_s - 1
    # max, min
    return (r_s, l_s)

def insert(l, m):
    ma = m[0]
    if len(l) == 0:
        return [m]
    for i in range(len(l)):
        if ma==l[i][0]:
            l[i] = (l[i][0], l[i][1] + m[1])
            return l
        elif ma>l[i][0]:
            return l[:i] + [m] + l[i:]
        elif ma<l[i][0]:
            continue
    l.append(m)
    return l

def solution(n, k):
    # n and l(repeat times)
    l = [(n, 1)]
    while k>0:
        cur = l.pop(0)
        x = cur[1]
        ma, mi = next_p(cur[0])
        if ma == mi:
            l = insert(l, (ma, x*2))
        else:
            l = insert(l, (ma, x))
            l = insert(l, (mi, x))
        k -= x
    return ma, mi

K = int(input())
for i in range(K):
    n, k = input().split()
    ma, mi = solution(int(n), int(k))
    print('Case #{0}: {1} {2}'.format(i+1, ma, mi))
