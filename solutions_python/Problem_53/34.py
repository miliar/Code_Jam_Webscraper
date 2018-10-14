def solve(N, K):
    if (K + 1) % 2 ** N == 0:
        return "ON"
    else:
        return "OFF"

def main():
    for i in range(int(input())):
        N, K = map(int, input().split())
        print("Case #{}:".format(i + 1), solve(N, K))

if __name__ == "__main__":
    main()

