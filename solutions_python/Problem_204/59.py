import math

def solve(n, p, r, q):
    result = 0
    dict = []
    for i in range(n):
        for j in range(p):
            dict.append({'n': i, 'div': q[i][j] / r[i], 'q': q[i][j]})
    dict.sort(key = lambda x: x['div'])

    queue =[[] for _ in range(n)]

    for i in range(n*p):
        queue[dict[i]['n']].append(dict[i])

        originalV = math.ceil(dict[i]['q']/1.1/r[dict[i]['n']])
        minV = originalV * 0.9
        count = 0
        for j in range(n):
            while True:
                if len(queue[j]):
                    #print (originalV, minV)
                    #print (queue, queue[j])
                    if queue[j][0]['q'] < minV*r[j]:
                        del queue[j][0]
                    else:
                        count += 1
                        break
                else:
                    break
        if count == n:
            result += 1
            for j in range(n):
                del queue[j][0]
    return result



T = int(input())
for t in range(1, T+1):
    N, P = [int(x) for x in input().split()]
    R = [int(x) for x in input().split()]
    Q = []
    for i in range(N):
        Q.append([int(x) for x in input().split()])

    print ('Case #{}: {}'.format(t, solve(N, P, R, Q)))
