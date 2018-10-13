def FindOptimalStall(S):
    idx = -1
    finalLeft = -1
    finalRight = -1
    for i in range(len(S)):
        if not S[i]:
            left = i
            while left >= 0 and not S[left]:
                left -= 1
            left = i - left  - 1
            right = i
            while right < len(S) and not S[right]:
                right += 1
            right = right - i - 1

            if min(left, right) > min(finalLeft, finalRight):
                idx = i
                finalLeft, finalRight = left, right
            elif min(left, right) == min(finalLeft, finalRight) and max(left, right) > max(finalLeft, finalRight):
               idx = i
               finalLeft, finalRight = left, right
    return idx, finalLeft, finalRight

def Solve(N, K):
    arr = [False] * N
    while K > 0:
        idx, left, right = FindOptimalStall(arr)
        arr[idx] = True
        K -= 1
    return max(0, max(left, right)), max(0, min(left, right))

numOfLines = int(raw_input())
for i in range(numOfLines):
    N, K = [int(x) for x in raw_input().split()]
    print "Case #" + str(i + 1) + ": " + " ".join(str(x) for x in Solve(N, K))
