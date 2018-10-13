def solve(R, k, N, groups):
    total = 0
    succ = {}
    i = 0
    for ride in range(R):
        if i in succ:
            s, j = succ[i]
            loop = 1
            while j != i:
                s += succ[j][0]
                j = succ[j][1]
                loop += 1
            rem = R - ride
            total += (rem // loop) * s
            rem = rem % loop
            for k in range(rem):
                total += succ[i][0]
                i = succ[i][1]
            break
        else:
            s = groups[i]
            j = (i + 1) % N
            while s + groups[j] <= k and j != i:
                s += groups[j]
                j = (j + 1) % N
            succ[i] = (s, j)
            total += s
            i = j
    return total

def main():
    for i in range(int(input())):
        R, k, N = map(int, input().split())
        groups = list(map(int, input().split()))
        print("Case #{}:".format(i + 1), solve(R, k, N, groups))

if __name__ == "__main__":
    main()

