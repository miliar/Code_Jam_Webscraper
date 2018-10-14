def solve(infile):
    input = open(infile)
    T = int(input.readline())
    for t in xrange(1, T+1):
        inputline = input.readline().split()
        next = 0
        C = int(inputline[next])
        next += 1
        combine = {}
        for _ in xrange(C):
            combine[inputline[next][:2]] = inputline[next][-1]
            combine[inputline[next][1::-1]] = inputline[next][-1]
            next += 1
        D = int(inputline[next])
        next += 1
        oppose = []
        for _ in xrange(D):
            oppose.append(inputline[next])
            oppose.append(inputline[next][::-1])
            next += 1
        N = int(inputline[next])
        next += 1
        elements = inputline[next]
        result = []
        for n in xrange(N):
            result.append(elements[n])
            if len(result) > 1:
                com = ''.join(result[-2:])
                if com in combine:
                    result = result[:-2] + list(combine[com])
                    continue
            for opp in oppose:
                if opp[0] in result and opp[1] in result:
                    result = []
        formatted_result = ""
        for i, r in enumerate(result):
            if i == 0:
                formatted_result += r
            else:
                formatted_result += ", " + r
        print "Case #%d: [%s]" % (t, formatted_result)
    input.close()
    
if __name__ == '__main__':
    import sys
    solve(sys.argv[1])