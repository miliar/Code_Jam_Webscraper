def happy(s):
    return all(c == '+' for c in s)


def solve(s, k):
    """Return the number of flips to make all pancakes happy"""
    if happy(s):
        return 0

    ss = list(s)
    count = 0
    for i in range(len(ss)-k+1):
        if ss[i] == '-':
            count += 1
            for j in range(i, i+k):
                if ss[j] == "-":
                    ss[j] = "+"
                else:
                    ss[j] = "-"

    if happy(ss[-k:]):
        return count
    return "IMPOSSIBLE"



if __name__ == "__main__":
    for t in range(int(input())):
        s, k = input().split()
        ans = solve(s, int(k))
        print("Case #{}: {}".format(t+1, ans))