#! coding: utf-8
import math
if __name__ == '__main__':

    #python2:
    T = int(raw_input())
    for i in xrange(T):
        N, K = [int(s) for s in raw_input().split(" ")]
        data = []
        for j in xrange(N):
            r, h = [int(s) for s in raw_input().split(" ")]
            data.append([r, h])

        res = 0
        data.sort(key=lambda x: x[0], reverse=True)
        for j in xrange(N - K + 1):
            s = math.pi * data[j][0] *(data[j][0] + 2 * data[j][1])
            part_data = data[j + 1:]
            part_data.sort(key=lambda x: x[0] * x[1], reverse=True)
            for l in xrange(K - 1):
                s += 2 * math.pi * part_data[l][0] * part_data[l][1]
            if s > res:
                res = s
        print("Case #{0}: {1}".format(i + 1, res))
