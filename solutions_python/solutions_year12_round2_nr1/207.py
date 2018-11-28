if __name__ == '__main__':
    #f = open('sample.in')
    #output = open('sample.out', 'w')
    f = open('A-large.in')
    output = open('A-small-attempt6.out', 'w')
    test_case = int(f.readline())
    for i in range(test_case):
        line = f.readline()
        line = line.split()
        N = int(line[0])
        line = line[1:]
        line = [int(line[j]) for j in range(N)]
        s = 'Case #%s: ' %(i+1)
        #for j in range(N):
            #if line[j] == 0:
                #line[j] = 0.000001
        total = sum(line)
        d = {}
        exclude = []
        for j in range(N):
            #front = 0
            #tail = 10000000
            #while tail - front > 10:
                #r = (tail + front) / 2

                #per = 0.0000001 * r
                #total_per = 0
                #for k in range(N):
                    #if k != j:
                        #y_k = (line[j] + total * per - line[k]) * 1.0 / total
                        #if y_k < 0:
                            #y_k = 0
                        #total_per += y_k
                #total_per += per
                #if total_per >= 1:
                    #tail = r
                #else:
                    #fornt = r
            per = 2.0 / N - line[j] * 1.0 / total
            #if per < 0:
                #d[j] = 0
                #line.remove(line[j])
            d[j] = per
        has_neg = False
        total *= 2
        raw = sum(line)
        for j in range(N):
            if d[j] < 0:
                d[j] = 0
                total -= line[j]
                exclude.append(j)
                has_neg = True
        while has_neg:
            has_neg = False
            for j in range(N):
                if not j in exclude:
                    d[j] = (total * 1.0 / (N - len(exclude)) - line[j])* 1.0 / raw
            for j in range(N):
                if d[j] < 0:
                    d[j] = 0
                    total -= line[j]
                    exclude.append(j)
                    has_neg = True
        for j in range(N):
            #per_total = sum(d.values())
            #per = d[j] * 1.0 / per_total
            per = d[j]
            s += str(per * 100) + ' '
        s += '\n'
        output.write(s)
    f.close()
    output.close()