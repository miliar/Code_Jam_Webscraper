# coding: utf-8


def check(n):
    ds = [int(c) for c in str(n)]
    for i in range(len(ds)-1):
        if not ds[i] <= ds[i + 1]:
            return False
    return True


def solve(n):
    ds = [int(c) for c in str(n)]
    for i in range(0, len(ds) - 1):
        if ds[i] > ds[i + 1]:
            ds[i] -= 1
            for j in range(i + 1, len(ds)):
                ds[j] = 9
            for j in range(i-1, -1, -1):
                if ds[j] > ds[j + 1]:
                    ds[j] -= 1
                    ds[j + 1] = 9
                else:
                    break
            break
    return int("".join(map(str, ds)))


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print("Case #{}: {}".format(i + 1, solve(n)))


if __name__ == "__main__":
    main()
