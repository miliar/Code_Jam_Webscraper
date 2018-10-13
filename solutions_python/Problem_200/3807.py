
def solve(N):
    while(True):
        length =len(N)
        for i in range(length):
            if i < length-1 and int(N[i]) > int(N[i+1]):
                break
            if i == length-1:
                return N

        N = str(int(N) - 1)

t = int(input())
for i in range(1, t + 1):
    N = input()
    n = solve(N)
    print("Case #{}: {}".format(i, n))
