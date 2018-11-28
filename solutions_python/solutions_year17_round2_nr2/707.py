d1 = dict()
d1[0] = 'R'
d1[1] = 'Y'
d1[2] = 'B'

ncase = int(raw_input())

for cidx in range(ncase):
    inp = map(int, raw_input().split())
    inp.pop(0)
    ryb = [inp[0], inp[2], inp[4]]
    ogv = [inp[1], inp[3], inp[5]]
    result = []

    tryb = list(ryb)
    last = -1
    counter = 0

    mode = 's'

    while sum(ryb) != 0:
        if mode == 'e' or counter % 2 == 0:
            i = ryb.index(max(ryb))
        else:
            i = ryb.index(min(ryb))
        if i == last:
            for j in range(3):
                i = (i + 1) % 3
                if ryb[i] != 0 and i != last:
                    break
        if ryb[i] == 0:
            counter += 1
            continue
        result.append(d1[i])
        ryb[i] -= 1
        last = i
        counter += 1
        if mode == 's':
            tryb = list(ryb)
            tryb.sort(reverse=True)
            if tryb[0] == tryb[1]:
                mode = 'e'

    imp = False
    if result[0] == result[len(result) - 1]:
        tmp = result[len(result) - 1]
        result[len(result) - 1] = result[len(result) - 2]
        result[len(result) - 2] = tmp

    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            imp = True
            break

    if imp:
        print "Case #{}: IMPOSSIBLE".format(cidx + 1)
        # print "Case #{}: {}".format(cidx + 1, ''.join(map(str, result)))
    else:
        print "Case #{}: {}".format(cidx + 1, ''.join(map(str, result)))

counter = 0
