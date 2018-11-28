import math

tests = []


def color_code(i):
    return ['R', 'O', 'Y', 'G', 'B', 'V'][i]


with open('input.in', 'r') as f:
    T = int(f.readline())
    for i in range(T):
        line = f.readline().strip().split(' ')
        N = int(line[0])
        counts = [int(k) for k in line[1:]]
        tests.append((N, counts))

with open('output.out', 'w') as f:
    case = 1
    for N, counts in tests:
        newN = N - 2*(counts[1] + counts[3] + counts[5])
        counts[4] -= counts[1]
        counts[2] -= counts[5]
        counts[0] -= counts[3]

        if counts[0] > newN/2 or counts[2] > newN/2 or counts[4] > newN/2 or counts[0] < 0 or counts[2] < 0 or counts[4] < 0 or newN < 0:
            f.write("Case #%d: IMPOSSIBLE\n" % (case))
        else:
            if counts[0] == 0 and counts[3] != 0:
                if (counts[1] > 0 or counts[2] > 0 or counts[4] > 0 or counts[5] > 0):
                    f.write("Case #%d: IMPOSSIBLE\n" % (case))
                else:
                    f.write("Case #%d: %s\n" % (case, 'RG' * counts[3]))
                case += 1
                continue
            if counts[2] == 0 and counts[5] != 0:
                if (counts[0] > 0 or counts[1] > 0 or counts[3] > 0 or counts[4] > 0):
                    f.write("Case #%d: IMPOSSIBLE\n" % (case))
                else:
                    f.write("Case #%d: %s\n" % (case, 'YV' * counts[5]))
                case += 1
                continue
            if counts[4] == 0 and counts[1] != 0:
                if (counts[0] > 0 or counts[2] > 0 or counts[3] > 0 or counts[5] > 0):
                    f.write("Case #%d: IMPOSSIBLE\n" % (case))
                else:
                    f.write("Case #%d: %s\n" % (case, 'OB' * counts[1]))
                case += 1
                continue


            if counts[0] >= counts[2] and counts[0] >= counts[4]:
                m = 0
            elif counts[2] >= counts[4]:
                m = 2
            else:
                m = 4

            high = m
            first = ((m - 2) % 6)
            last = ((m + 2) % 6)

            result = [None] * newN

            for i in range(counts[first]):
                result[2*i + 1] = color_code(first)
            for i in range(counts[last]):
                if result[newN - 2 * i - 1] == None:
                    result[newN - 2 * i - 1] = color_code(last)
                else:
                    result[newN - 2 * i - 2] = color_code(last)

            for i in range(len(result)):
                if result[i] == None:
                    result[i] = color_code(high)

            for i in range(counts[1]):
                idx = result.index('B')
                result.insert(idx, 'O')
                result.insert(idx, 'B')

            for i in range(counts[3]):
                idx = result.index('R')
                result.insert(idx, 'G')
                result.insert(idx, 'R')

            for i in range(counts[5]):
                idx = result.index('Y')
                result.insert(idx, 'V')
                result.insert(idx, 'Y')

            result =''.join(result)

            f.write("Case #%d: %s\n" % (case, result))

        case += 1




        #for i, quans in pos_ans.items():
        #    print("%d %s" % (i, quans))
        #    if len(quans) == N:
        #        ans += min(quans.values())
        #print()
        #f.write("Case #%d: %d\n" % (case, ans))
        #case += 1




