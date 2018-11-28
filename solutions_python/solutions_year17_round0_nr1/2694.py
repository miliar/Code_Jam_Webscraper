tests = int(raw_input())

for test in range(1, tests+1):
    count = 0
    arr, k = raw_input().split(" ")
    arr = list(arr)
    k = int(k)
    index = 0
    while index+k-1 < len(arr):
        if arr[index] == '-':
            count += 1
            for i in range(index, index+k):
                if arr[i] == '+':
                    arr[i] = '-'
                else:
                    arr[i] = '+'
        #print arr, arr[index]
        index += 1

    while index < len(arr):
        if arr[index] == "-":
            print "Case #%s: IMPOSSIBLE"%(str(test))
            break
        index += 1
    if index == len(arr):
        print "Case #%s: %s"%(str(test), str(count))
