import math

def main():
    t = int(input())
    vals = []
    for i in range(0, t):
        line = input()
        nums = line.split()
        n = int(nums[0])
        k = int(nums[1])
        vals.append([n, k])
    i = 1

    for val in vals:
        n = val[0]
        k = val[1]
        result = stall_min_max(n, k)
        print("Case #{0}: {1} {2}".format(i, result[0], result[1]))
        i += 1
        #print(result)

def stall_min_max(n, k):
    if k == 1:
        return (math.ceil((n-1)/2), math.floor((n-1)/2))


    if k % 2 == 0:
        return stall_min_max(math.ceil((n-1)/2), k // 2)
    else:
        return stall_min_max(math.floor((n-1)/2), k // 2)

main()
