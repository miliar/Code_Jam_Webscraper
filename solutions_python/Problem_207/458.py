from collections import Counter

t = int(input())


def solve(n, r, o, y, g, b, v):
    highest, *others = sorted([r, y, b], reverse=True)
    if highest > sum(others):
        return "IMPOSSIBLE"
    answer = ""
    colors = Counter({"R": r, "Y": y, "B": b})
    while n:
        for color, count in colors.most_common():
            if not count:
                continue
            if not answer.endswith(color):
                answer += color
                colors[color] -= 1
                n -= 1
                break
    if answer[0] == answer[-1]:
            answer = answer[:-2] + answer[-1] + answer[-2]
    assert answer[0] != answer[-1], answer[:4] + "-" + answer[-4:]
    return answer


for case in range(1, t+1):
    n, r, o, y, g, b, v = map(int, input().split())

    answer = solve(n, r, o, y, g, b, v)
    print(f"Case #{case}: {answer}")

