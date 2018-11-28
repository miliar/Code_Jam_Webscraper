def solve(combos, opposing, series):
    series = list(series)
    output = []
    while series:
        el = series.pop(0)
        if opposing.get(el) in output:
            output = []
        elif series and el+series[0] in combos:
            output.append(combos[el+series[0]])
            series.pop(0)
        else:
            output.append(el)
    return '[' + ", ".join(output) + ']'

t = int(input())
for case in range(t):
    line = input().split(' ')
    c = int(line.pop(0))
    combos = {}
    for combo in line[:c]:
        combos[combo[:2]] = combo[2]
        combos[combo[1]+combo[0]] = combo[2]
    d = int(line[c])
    opposing = {}
    for op in line[c+1:c+1+d]:
        opposing[op[0]] = op[1]
        opposing[op[1]] = op[0]
    series = line[c+1+d+1]
    print("Case #%d:" % (case+1), solve(combos, opposing, series))

