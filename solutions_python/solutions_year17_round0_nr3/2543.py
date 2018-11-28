from bisect import bisect_left, bisect_right, insort_left
import time

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    if n != k:
        stalls = [0 for i in range(n + 2)]
        stalls[0] = -1
        stalls[len(stalls) - 1] = -1
        occupied = [0, len(stalls) - 1]
        for p in range(k):
            fmin = 0
            fmax = 0
            min_set = []
            max_1 = 0
            # print(occupied)
            for j, k in enumerate(stalls):
                # print(stalls[j],"====",occupied)
                if stalls[j] != -1:
                    r = find_lt(occupied,j)
                    # while(stalls[r]!=-1):
                    #     r -= 1
                    # mx = [s for s in occupied if s < j]
                    # print(mx,"max")
                    left = j - r - 1
                    # else:
                    #     left = j - 1
                    r = find_gt(occupied,j)
                    # while(stalls[r]!=-1):
                    #     r += 1
                    # mi = [s for s in occupied if s > j]
                    # print(mi,"min")
                    # if mi:
                    right = r - (j + 1)
                    # else:
                    #     right = j + 1

                    if(min(left, right) > max_1):
                        max_1 = min(left, right)
                    min_set.append((j, left, right))
            # print(min_set)
            max_set = []
            max_2 = 0
            # print(min_set)
            for y in min_set:
                if(min(y[1], y[2]) == max_1):
                    max_set.append(y)

            final = []
            # print(max_set,max_1)
            # # print(max_set,max_2)
            for z in max_set:
                # print(z)
                if(max(z[1], z[2]) > max_2):
                    max_2 = max(z[1], z[2])
            for t in max_set:
                if(max(t[1], t[2]) == max_2):
                    final.append(t)
            stalls[final[0][0]] = -1
            # occupied.append(final[0][0])
            insort_left(occupied,final[0][0])
            # print(final[0], "-")
            fmin = min(final[0][1], final[0][2])
            fmax = max(final[0][1], final[0][2])
    else:
        fmin = 0
        fmax = 0
    print("Case #{}: {} {}".format(i, fmax, fmin))
