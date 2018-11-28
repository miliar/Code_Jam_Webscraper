T = int(input())
num = T

def largest(a):
    l = [-1]
    if 1 not in a: return (0, len(a))
    elif a.count(1) == 1:
        if len(a[:a.index(1)]) < len(a[a.index(1) + 1:]):
            return (a.index(1) + 1, len(a))
        else: return (0, a.index(1))
    else:
        for i in range(len(a)):
            if a[i] == 1: l.append(i)
        l.append(len(a) + 1)
        max = 0
        slice = [0,0]
        for i in range(len(l) - 1):
            if l[i+1] - l[i] > max:
                max = l[i+1] - l[i]
                slice = [l[i],l[i+1]]
        return (slice[0], slice[1])



while T:
    T -= 1
    case = num - T
    [n,k] = input().split()
    k = int(k)
    n = int(n)
    a = [0] * n
    if n == k:
        print("Case #" + str(case) + ": 0 0")
        continue
    while k > 0:
        k -= 1
        (lower, upper) = largest(a)
        a[(upper + lower)//2] = 1
        if (upper + lower)//2 == 0: l = 0
        else:
            for i in range((upper + lower)//2 - 1, -1, -1):
                if a[i] == 1:
                    l = (upper + lower)//2 - i - 1
                    break
                l = (upper + lower)//2
        if (upper + lower)//2 == len(a) - 1: u = 0
        else:
            for i in range((upper + lower) // 2 + 1, len(a)):
                if a[i] == 1:
                    u = i - (upper + lower) // 2 - 1
                    break
                u = len(a) - (upper + lower) // 2 - 1
        #print(a)
    if l<u: l,u = u,l
    print("Case #" + str(case) + ": " + str(l) + ' ' + str(u))