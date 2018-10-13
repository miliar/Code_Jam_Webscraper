def solution(n, r, o, y, g, b, v):
    # if r <= g or b <= o or y <= v:
    #     return 'IMPOSSIBLE'

    if r == g and o + y + b + v == 0:
        return 'RG' * r
    if b == o and n - b - o == 0:
        return 'BO' * b
    if y == v and n - y - v == 0:
        return 'YV' * y

    rg = 'RG' * g + 'R'
    bo = 'BO' * o + 'B'
    yv = 'YV' * v + 'Y'
    r -= g
    b -= o
    y -= v


    if r > b + y or b > r + y or y > r + b:
        return 'IMPOSSIBLE'

    result = ''
    l = [['R', r], ['B', b], ['Y', y]]#.sort(key=lambda x: x[1], reverse=True)
    l.sort(key=lambda x: x[1], reverse=True)
    l[0][1] += 1
    cnt = r + b + y
    ptr = 0

    while cnt >= 0:
        result += l[ptr][0]
        l[ptr][1] -= 1
        if l[ptr][1] < 0:
            return 'IMPOSSIBLE'

        v1 = (ptr + 1) % 3
        v2 = (ptr + 2) % 3
        if l[v1][1] > l[v2][1]:
            ptr = v1
        else:
            ptr = v2

        cnt -= 1

    if len(result) > 1:
        result = result[:-1]

    if len(rg) > 1:
        for i in range(len(result)):
            if result[i] == 'R':
                result = result[:i] + rg + result[i+1:]
    if len(bo) > 1:
        for i in range(len(result)):
            if result[i] == 'B':
                result = result[:i] + bo + result[i+1:]
    if len(yv) > 1:
        for i in range(len(result)):
            if result[i] == 'Y':
                result = result[:i] + yv + result[i+1:]

    return result

t = int(input())

for i in range(t):
    n, r, o, y, g, b, v = map(int, input().split())
    print("Case #%d: %s" % (i+1, solution(n, r, o, y, g, b, v)))
