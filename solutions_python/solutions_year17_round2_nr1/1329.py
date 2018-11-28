def solve(d, n, s):
    slowest = 0

    for horse in s:
        slowest = max((d - horse[0]) / float(horse[1]), slowest)

    return d / slowest

def main():
    t = int(input())
    for i in range(1, t + 1):
        d, n = [int(s) for s in input().split(" ")]
        s = []
        for j in range(n):
            s.append([int(s) for s in input().split(" ")])

        print(f"Case #{i}: {solve(d, n, s)}")


if __name__ == "__main__": main()