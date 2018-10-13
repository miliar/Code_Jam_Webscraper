from functools import reduce

def solve(n):
    n = [int(elem) for elem in str(n)]
    for i in range(len(n)-1,0,-1):
        if n[i-1] > n[i]:
            n[i:] = [9] * len(n[i:])
            n[i-1] -= 1

    return int(reduce(lambda x, y: x + str(y), n, ''))

# print(solve(132))
# print(solve(1000))
# print(solve(7))
# print(solve(111111111111111110))
# exit(0)

t = int(input())
for i in range(1, t+1):
    n = input()
    print("Case #{}: {}".format(i, solve(n)))