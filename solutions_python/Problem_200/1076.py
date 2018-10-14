



T = raw_input()
T = int(T)

for i in range(T):
    N = raw_input()
    arr = [ int(x) for x in N ]
    #print(arr)
    
    l = len(arr)
    start = 0
    for j in range(l-1):
        if arr[j] == arr[j+1]:
            continue

        if arr[j] < arr[j+1]:
            start = j + 1
            continue

        if arr[j] > arr[j+1]:
            arr[start] = arr[start] - 1
            for k in range(start+1, l):
                arr[k] = 9
            break
    for j in range(l):
        if arr[j] != 0:
            arr = arr[j:]
            break

    print("Case #%d: %s" % (i+1, ''.join([str(x) for x in arr])))

