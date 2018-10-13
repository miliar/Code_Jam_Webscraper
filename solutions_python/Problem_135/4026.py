t = int(raw_input())
for tt in range(t):
    n = int(raw_input())
    arr = []
    arr.append(map(int, raw_input().split()))
    arr.append(map(int, raw_input().split()))
    arr.append(map(int, raw_input().split()))
    arr.append(map(int, raw_input().split()))
    m = int(raw_input())
    arr2 = []
    arr2.append(map(int, raw_input().split()))
    arr2.append(map(int, raw_input().split()))
    arr2.append(map(int, raw_input().split()))
    arr2.append(map(int, raw_input().split()))
    x = set(arr[n-1]) & set(arr2[m-1])
    if len(x) == 0:
        print "Case #{0}: Volunteer cheated!".format(tt+1)
    elif len(x) == 1:
        print "Case #{0}: {1}".format(tt+1, x.pop())
    else:
        print "Case #{0}: Bad magician!".format(tt+1)
