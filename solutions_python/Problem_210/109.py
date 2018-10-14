in_file = 'B-large.in'
out_file = 'B-large.out'
inp = open(in_file, 'r')
out = open(out_file, 'w')

t = int(inp.readline())
for case in range(1, t+1):
    ac, aj = list(map(int, inp.readline().split()))
    c = []
    d = []
    j = []
    k = []
    combined = []

    for i in range(ac):
        x, y = list(map(int, inp.readline().split()))
        c.append(x)
        d.append(y)
        combined.append(x)
    for i in range(aj):
        x, y = list(map(int, inp.readline().split()))
        j.append(x)
        k.append(y)
        combined.append(x)

    c.sort()
    d.sort()
    j.sort()
    k.sort()
    combined.sort()

    switches = 0
    total_c = 0
    total_j = 0
    gap_c = []
    gap_j = []
    if combined[0] in c:
        last = c
        total_c = d[0] - c[0]
    else:
        last = j
        total_j = k[0] - j[0]

    for activity in combined[1:]:
        if activity in c:
            index = c.index(activity)
            if last == c:
                total_c += d[index] - d[index-1]
                gap_c.append(c[index] - d[index-1])
            else:
                total_c += d[index] - c[index]
                switches += 1
                last = c
        if activity in j:
            index = j.index(activity)
            if last == j:
                total_j += k[index] - k[index-1]
                gap_j.append(j[index] - k[index-1])
            else:
                total_j += k[index] - j[index]
                switches += 1
                last = j

    if combined[-1] in c:
        if combined[0] in c:
            total_c += 1440 - d[-1] + c[0]
            gap_c.append(1440 - d[-1] + c[0])
        if combined[0] in j:
            switches += 1
    if combined[-1] in j:
        if combined[0] in j:
            total_j += 1440 - k[-1] + j[0]
            gap_j.append(1440 - k[-1] + j[0])
        if combined[0] in c:
            switches += 1

    if total_c > 720:
        gap_c.sort(reverse=True)
        for gap in gap_c:
            total_c -= gap
            switches += 2
            if total_c <= 720:
                break
    if total_j > 720:
        gap_j.sort(reverse=True)
        for gap in gap_j:
            total_j -= gap
            switches += 2
            if total_j <= 720:
                break

    out.write('Case #{}: {}\n'.format(case, switches))

inp.close()
out.close()
