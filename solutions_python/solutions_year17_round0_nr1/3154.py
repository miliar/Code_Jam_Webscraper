import sys
cases = int(sys.stdin.readline())
for count in range(cases):
    arr=[]
    ch = sys.stdin.read(1)
    while ch != ' ':
        arr.append(ch)
        ch = sys.stdin.read(1)
    sz = int(sys.stdin.readline())
    marker = 0
    flips = 0
    while (marker + sz) <= len(arr):
        if arr[marker]=='-':
            flips += 1
            for i in range(sz):
                arr[marker+i] = '+' if arr[marker+i] == '-' else '-'
        marker += 1
    possible = True
    while marker < len(arr) and possible:
        if arr[marker] == '-':
            possible = False
        marker += 1
    if possible:
        print "Case #%s: %s"%(count+1,flips)
    else:
        print "Case #%s: IMPOSSIBLE"%(count+1)
