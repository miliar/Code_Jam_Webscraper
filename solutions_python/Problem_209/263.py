import math

def solve(pancakes, k):
    pancakes.sort(key=lambda tup: tup[0], reverse=True)

    best = 0
    for idx, val in enumerate(pancakes):
        result = math.pi * (val[0]*val[0]) + 2*math.pi*val[0]*val[1]
        rest_pancakes = pancakes[idx + 1:]
        if len(rest_pancakes) < k - 1:
            continue
        rest_pancakes.sort(key=lambda tup: 2*math.pi*tup[0]*tup[1], reverse=True)
        for i in range(k - 1):
            result += 2*math.pi*rest_pancakes[i][0]*rest_pancakes[i][1]

        best = max(best, result)

    return best


def main():
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        s = []
        for j in range(n):
            s.append([int(s) for s in input().split(" ")])

        print(f"Case #{i}: {solve(s, k)}")


if __name__ == "__main__": main()