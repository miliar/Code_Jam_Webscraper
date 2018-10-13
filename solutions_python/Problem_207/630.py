def answer(left, horses, colors):
    copy = horses[:]
    m = max(copy)
    copy.remove(m)
    if sum(copy) < m:
        return "IMPOSSIBLE"
    else:
        i = horses.index(m)
        max_color = colors[i]
        colors = colors.replace(max_color, 'z')
        horses = list(map(list, zip(horses, colors)))
        horses.sort(reverse=True)
        i = 0
        stables = [horses[i][1]]
        left -= 1
        horses[i][0] -= 1

    for _ in range(left):
        horses.sort(reverse=True)

        i = 0 if stables[-1] != horses[0][1] else 1

        if horses[i][0] == 0:
            return "IMPOSSIBLE"
        else:
            stables.append(horses[i][1])
            horses[i][0] -= 1

    return "".join(stables).replace('z', max_color)

def case_print(case, result):
    print("Case #" + str(case) + ":", result)
    #print(result)

# R, O, Y, G, B, and V
if __name__ == "__main__":
    n = int(input())
    for c in range(n):
        line = list(map(int, input().split()))
        left = line[0]
        horses = line[1:]
        case_print(c + 1, answer(left, horses, "ROYGBV"))
