colors = 'ROYGBV'
easycolors = 'RYB'

ret = []
with open('B-small-attempt1.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        d = list(map(int, file.readline().split()))
        n = d[0]
        horses = d[1:]

        #Small
        easyhorses = [d[1], d[3], d[5]]
        tret = []
        last = None
        if d[1] >= d[3]:
            if d[1] >= d[5]:
                first = 0
            else:
                if d[3] >= d[5]:
                    first = 1
                else:
                    first = 2
        else:
            if d[3] >= d[5]:
                first = 1
            else:
                first = 2

        for i in range(n):

            candidate = None
            for j in range(3):
                if j == last:
                    continue
                if easyhorses[j]:
                    if candidate is None:
                        candidate = j
                    elif easyhorses[candidate] < easyhorses[j]:
                        candidate = j
                    elif easyhorses[candidate] == easyhorses[j]:
                        if j == first:
                            candidate = j

            if candidate is not None:
                tret.append(candidate)
                last = candidate
                easyhorses[candidate] -= 1
            else:
                ret.append('IMPOSSIBLE')
                break
        else:
            if tret[0] == tret[-1]:
                ret.append('IMPOSSIBLE')
            else:
                ret.append(''.join(map(lambda x: easycolors[x], tret)))

        assert first == tret[0]


with open('Bout-small1.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" %(i+1, ret[i]))