def opposite(symb):
    if symb == '+':
        return '-'
    return '+'

def flip(l, pos, length):
    res = []
    for index, elem in enumerate(l):
        if index >= pos and index < (pos + length):
            res.append(opposite(elem))
        else:
            res.append(elem)
    return res

with open('A-large.in') as inp:
    with open('output.txt', 'w') as outp:
        ncases = int(inp.readline().strip())
        for nc in range(0, ncases):
            line = inp.readline().strip().split(' ')
            l = [char for char in line[0]]
            length = int(line[1])

            if(len(l) < length):
                outp.write("Case #{}: IMPOSSIBLE\n".format(nc + 1))
                continue

            count = 0
            for idx in range(0, len(l) - length + 1):
                if l[idx] == '-':
                    l = flip(l, idx, length)
                    count += 1

            flag = False
            for symb in l:
                if(symb == '-'):
                    flag = True
            if flag:
                outp.write("Case #{}: IMPOSSIBLE\n".format(nc + 1))
                continue

            outp.write("Case #{}: {}\n".format(nc + 1, count))