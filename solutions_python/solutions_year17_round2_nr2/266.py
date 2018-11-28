
def solve(n, colors):
    # nColDif = colors.count(0)
    labels = ['R', 'O', 'Y', 'G', 'B', 'V']
    colors = [[num, labels[i]] for (i, num) in enumerate(colors)]
    colors = sorted(colors, reverse=True)
    if colors[0][0] * 2 > n:
        return "IMPOSSIBLE"
    solucio = [colors[0][1]]
    colors[0][0] -= 1
    for i in range(n - 3): # nomes R, Y, B
        colors = sorted(colors, reverse=True)
        j = 0
        while solucio[-1] == colors[j][1]:
            j += 1
        solucio.append(colors[j][1])
        colors[j][0] -= 1

    colors = sorted(colors, reverse=True)
    if colors[0][1] == solucio[0]:
        solucio.append(colors[0][1])
        solucio.append(colors[1][1])
    else: # elif colors[1][1] == solucio[0]:
        solucio.append(colors[1][1])
        solucio.append(colors[0][1])

    return ''.join(solucio)

t = int(input())
for i in range(1, t+1):
    line = input()
    n = int(line.split(" ")[0])
    colors = []
    for num in line.split(" ")[1:]:
        colors.append(int(num))
    print("Case #{}:".format(i), solve(n, colors))