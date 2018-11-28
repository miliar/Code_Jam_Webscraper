def readInts():
    r = raw_input()
    s = r.split()
    return [int(ss) for ss in s]

def main():
    t = readInts()[0]
    
    fd = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    case = 1
    for tt in range(t):

        h, w = readInts()
        
        m = []
        sink = []
        result = []

        queue = []

        for i in range(h):
            m.append(readInts())
            sink.append([0 for i in range(w)])
            result.append([0 for i in range(w)])
            
        # print m

        # find flow
        for i in range(h):
            for j in range(w):
                smallest = 1000000
                for (dh, dw) in fd:
                    nh = i + dh
                    nw = j + dw
                    if (0 <= nh < h) and (0 <= nw < w):
                        if m[nh][nw] < m[i][j] and m[nh][nw] < smallest:
                            smallest = m[nh][nw]
                            sink[i][j] = nh, nw
                
                if smallest == 1000000:
                    sink[i][j] = i, j
                    result[i][j] = i, j
                    queue.append((i, j))

        # print sink
        # print queue

        # find real sink
        while queue:
            q = queue.pop()
            for (dh, dw) in fd:
                nh = q[0] + dh
                nw = q[1] + dw
                if (0 <= nh < h) and (0 <= nw < w):
                    if sink[nh][nw] == q:
                        queue.append((nh, nw))
                        result[nh][nw] = result[q[0]][q[1]]

        # print result

        dic = {}
        maxc = 'a'
        for i in range(h):
            for j in range(w):
                if result[i][j] not in dic.keys():
                    dic[result[i][j]] = maxc
                    maxc = chr(ord(maxc) + 1)

                sink[i][j] = dic[result[i][j]]

        print 'Case #%d:' % case
        case += 1
        for r in sink:
            for c in r:
                print c,
            print

if __name__ == '__main__':
    main()