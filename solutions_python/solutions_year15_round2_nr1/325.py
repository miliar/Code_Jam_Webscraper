a = [1000009]*1000002

a[0]=0

for i in range(1000001):
    a[i+1] = min(a[i+1], a[i]+1)
    try:
        a[int(str(i)[::-1])] = min(a[int(str(i)[::-1])], a[i]+1)
    except IndexError:
        pass

for case in range(1, int(input())+1):
    print("Case #{}: {}".format(case, a[int(input())]))