import sys
sys.stdout = open('file.out', 'w')


t = int(raw_input())  # read a line with a single integer
for test in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    stalls = [1]
    for __ in range(n):
        stalls.append(0)
    stalls.append(1)
    max_start = 0
    max_end = 0
    start = 0
    end = 0
    while k > 0:
        max_start = 0
        max_end = 0
        start = 0
        end = 0
        for i in range(1, len(stalls)):
            if stalls[i] == 1:
                end = i
                if end - start > max_end - max_start:
                    max_end, max_start = end, start
                start = i
        index = (max_end + max_start) / 2
        stalls[index] = 1
        k -= 1
    left = index - max_start - 1
    right = max_end - index - 1
    print "Case #{}: {} ".format(test, str(max(left,right)) + " " + str(min(left,right)))
