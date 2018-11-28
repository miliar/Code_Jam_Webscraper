def solve(smax, audiNums):
    ovationTotal = 0
    addtionalTotal = 0
    for s in range(0, smax+1):
        audiNum = int(audiNums[s:s+1])
        if ovationTotal >= s:
            ovationTotal += audiNum
        else:
            addtional = s - ovationTotal
            ovationTotal += (audiNum+addtional)
            addtionalTotal += addtional
    return addtionalTotal

def start():
    f = open('A-large.in', 'r')
    of = open('output.out', 'w')
    tn = int(f.readline())
    for t in range(1, tn+1):
        line = f.readline().rstrip().split()
        smax = int(line[0])
        audiNums = line[1]
        of.write("Case #{0}: {1}\n".format(t, solve(smax, audiNums)))
    f.close()
    of.close()

start()