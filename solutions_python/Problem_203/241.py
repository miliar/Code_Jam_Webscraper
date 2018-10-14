T = int(input())
for t in range(1, T + 1):
    R, C = [int(_) for _ in input().split()]
    output = []
    data = []
    for i in range(R):
        s = list(input())
        output.append(s)
        for j in range(C):
            if s[j] != '?':
                data.append([[j, i] for _ in range(2)])
    done = False
    while not done:
        done = True
        for ii in range(len(data)):
            flag = True
            while flag and data[ii][0][1] > 0:
                for i in range(data[ii][0][0], data[ii][1][0] + 1):
                    if output[data[ii][0][1] - 1][i] != '?':
                        flag = False
                        break
                if flag:
                    for i in range(data[ii][0][0], data[ii][1][0] + 1):
                        output[data[ii][0][1] - 1][i] = output[data[ii][0][1]][data[ii][0][0]]
                    data[ii][0][1] -= 1
                    done = False
            flag = True
            while flag and data[ii][0][0] > 0:
                for i in range(data[ii][0][1], data[ii][1][1] + 1):
                    if output[i][data[ii][0][0] - 1] != '?':
                        flag = False
                        break
                if flag:
                    for i in range(data[ii][0][1], data[ii][1][1] + 1):
                        output[i][data[ii][0][0] - 1] = output[data[ii][0][1]][data[ii][0][0]]
                    data[ii][0][0] -= 1
                    done = False
            flag = True
            while flag and data[ii][1][0] < C - 1:
                for i in range(data[ii][0][1], data[ii][1][1] + 1):
                    if output[i][data[ii][1][0] + 1] != '?':
                        flag = False
                        break
                if flag:
                    for i in range(data[ii][0][1], data[ii][1][1] + 1):
                        output[i][data[ii][1][0] + 1] = output[data[ii][0][1]][data[ii][0][0]]
                    data[ii][1][0] += 1
                    done = False
            flag = True
            while flag and data[ii][1][1] < R - 1:
                for i in range(data[ii][0][0], data[ii][1][0] + 1):
                    if output[data[ii][1][1] + 1][i] != '?':
                        flag = False
                        break
                if flag:
                    for i in range(data[ii][0][0], data[ii][1][0] + 1):
                        output[data[ii][1][1] + 1][i] = output[data[ii][0][1]][data[ii][0][0]]
                    data[ii][1][1] += 1
                    done = False
    print('Case #%d:' % t)
    for _ in range(R):
        print(''.join(output[_]))





