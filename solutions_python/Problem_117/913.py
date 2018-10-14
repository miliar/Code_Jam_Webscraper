def cut(m, table, i, row = True):
    data = None
    if row:
        data = table[i]
    else:
        data = [t[i] for t in table]
    return [e > m and m or e for e in data]

def main():
    test_cnt = int(raw_input())
    for count in xrange(test_cnt):
        N, M = [int(x) for x in raw_input().split()]
        read_t= []
        cutting = []
        for n in xrange(N):
            read_t.append([int(x) for x in raw_input().split()])
            cutting.append([100] * M)
        
        # row cutting
        for i, t in enumerate(read_t):
            data = cut(max(read_t[i]), cutting, i)
            cutting[i] = data

        # column cutting
        for i in xrange(M):
            data = [t[i] for t in read_t]
            data = cut(max(data), cutting, i, False)
            for j, t in enumerate(cutting):
                t[i] = data[j]

        for n in xrange(N):
            out = False
            for m in xrange(M):
                if read_t[n][m] != cutting[n][m]:
                    print 'Case #%d: NO' % (count + 1,)
                    out = True
                    break
            if out:
                break
        else:
            print 'Case #%d: YES' % (count + 1,)

if __name__ == '__main__':
    main()
