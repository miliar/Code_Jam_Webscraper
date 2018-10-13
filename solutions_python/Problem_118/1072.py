'''
if there's ao or tu in some row, then for the ao or tu point, the other line must all be lower than this
'''
import math

def palin(str):
    for i in range(len(str) / 2):
        if str[i] != str[len(str) - i - 1]:
            return 0
    return 1

T = int(raw_input())
for t in range(1, T + 1):
    A, B = map(int, raw_input().split())
    sqA = int(math.sqrt(A))
    if sqA * sqA < A: sqA += 1
    sqB = int(math.sqrt(B))
    
    cnt = 0
    for num in range(sqA, sqB + 1):
        s = str(num)
        ss = str(num * num)
        if palin(s) and palin(ss):
            cnt += 1

    print "Case #%d: %d" % (t, cnt) 

    
