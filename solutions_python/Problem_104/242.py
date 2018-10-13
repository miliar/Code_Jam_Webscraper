import itertools

def findsubsets(S, m):
    return set(itertools.combinations(S, m))

t = int(raw_input())
for i in range(t):
    arr = raw_input().split()
    nums = set([int(n) for n in arr[1:]])
    vals = {}
    n = int(arr[0])
    done = False
    for j in range(n):
        # Find size j subsets
        subsets = findsubsets(nums, j)
        for ss in subsets:
            if sum(ss) in vals:
                out1 = vals[sum(ss)]
                out2 = ss
                done = True
                break
            else:
                vals[sum(ss)] = ss

        if done:
            break

    print "Case #%s:" % (i+1)
    if done:
        print " ".join(map(str, out1))
        print " ".join(map(str, out2))
    else:
        print "Impossible"

