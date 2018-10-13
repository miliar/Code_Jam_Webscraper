def qsort(arr):
    if arr == []:
        return []
    if len(arr) == 1:
        return arr
    x = arr[0];
    low = qsort([i for i in arr[1:] if i <=x ])
    high = qsort([i for i in arr[1:] if i > x])
    return low + [x] + high

def solve(n, s, p, arr):
    if p - 2 < 0:
        s = 0
    p = p * 3
    arr = qsort(arr)
    temp = list(arr)
    for i in range(n):
        arr[i] = p - arr[i]
    arr = arr[::-1]
    temp = temp[::-1]
    i = 0
    while (i < n):
        if arr[i] <= 4 and arr[i] > 2:
            if s == 0:
                break
            
            s = s - 1

        if arr[i] > 4:
            break
        i += 1
    return i

f = input()
t = int(f)
for i in range(t):
    f = input()
    l1 = f.split()
    l2 = [int(i) for i in l1]
    result = solve(l2[0], l2[1], l2[2], l2[3:])
    print('Case #{0}: {1}'.format(i+1, result))
    


