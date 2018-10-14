for t in xrange(1,input()+1):
    arr,k = raw_input().split()
    k = int(k)
    arr = list(arr)
    ans = 0
    for i in xrange(len(arr)):
        if arr[i] == '-':
            if i + k > len(arr):
                ans = 'IMPOSSIBLE'
                break
            else:
                for j in xrange(i,i+k):
                    if arr[j] == '-':
                        arr[j] = '+'
                    else:
                        arr[j] = '-'
                ans += 1
    print "Case #{0}: {1}".format(t,ans)
