def solve():
    R, C = map(int, input().split())
    rprev = [None] * R
    cprev = [None] * C
    arrows = {}
    for r in range(R):
        l = input()
        for c in range(C):
            if l[c] in "^>v<":
                arrow = {"d": l[c], "^": cprev[c], "<": rprev[r], ">": None, "v": None}
                if cprev[c]:
                    cprev[c]["v"] = arrow
                if rprev[r]:
                    rprev[r][">"] = arrow
                cprev[c] = arrow
                rprev[r] = arrow
                arrows[(c, r)] = arrow
    count = 0
    for arrow in arrows.values():
        if arrow[arrow["d"]]:
            continue
        if arrow["^"] or arrow[">"] or arrow["v"] or arrow["<"]:
            count += 1
        else:
            return "IMPOSSIBLE"
    return count


tcnum = int(input())

for tc in range(1, tcnum+1):
    print("Case #{}: {}".format(tc, solve()))