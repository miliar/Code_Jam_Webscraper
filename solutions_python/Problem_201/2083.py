def empty(n, k):
    lst = []
    lst.append(int((n-1)/2))
    lst.append(n - (int((n-1)/2)) - 1)
    lst.sort(reverse=True)
    if k == 1:
        return lst
    j = 0
    while j < k-1:
        n = lst[j]
        a = int((n-1)/2)
        b = n - a - 1
        lst.append(a)
        lst.append(b)
        lst.sort(reverse=True)
        j += 1
        if j == k-1:
            return [max(a,b), min(a,b)]



for i in range(1, int(input())+1):
    n, k = map(int, input().split())
    print("Case #{}: {}".format(i, " ".join(map(str, empty(n, k)))))
