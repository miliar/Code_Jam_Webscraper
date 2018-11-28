import math

def solve(n, k):
    stalls = [0, n+1]
    for p in range(k):
        max_l = 0
        max_i = 0
        for i in range(1, len(stalls)):
            if stalls[i] - stalls[i-1] > max_l:
                max_l = stalls[i] - stalls[i-1]
                max_i = i
        stalls.insert(max_i, int(stalls[max_i] - (max_l/2)))
        if p == k-1:
            return (math.ceil(max_l/2)-1, max_l//2-1)

if __name__=="__main__":
    line_count = int(input())
    for i in range(1, line_count + 1):
        n, k = map(int, input().split(" "))
        result = solve(n, k)
        print("Case #{}:".format(i), *result)
