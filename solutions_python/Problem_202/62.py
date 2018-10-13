def f(n, models):
    rowFlags = [False]*n
    colFlags = [False]*n
    sumFlags = [False]*(2*n-1)
    diffFlags = [False]*(2*n-1)
    point = 0

    for pos, type in models.items():
        if type == 'o' or type == 'x':
            rowFlags[pos[0]] = True
            colFlags[pos[1]] = True

        if type == 'o' or type == '+':
            sumFlags[pos[0] + pos[1]] = True
            diffFlags[pos[0] - pos[1]] = True

        point += 2 if type == 'o' else 1

    newModels = {}

    rows = []
    cols = []

    for i in range(n):
        if not rowFlags[i]:
            rows.append(i)

        if not colFlags[i]:
            cols.append(i)

    assert len(rows) == len(cols)

    for i in range(len(rows)):
        newPos = (rows[i], cols[i])

        if newPos in models:
            if models[newPos] == '+':
                newModels[newPos] = 'o'
                models[newPos] = 'o'
                point += 1
        else:
            newModels[newPos] = 'x'
            models[newPos] = 'x'
            point += 1
                
    for i in range(2*n - 1):
        if sumFlags[i]:
            continue

        d = getD(diffFlags, n, i)
        if d != None:
            assert d%2 == i%2
            
            row = (i + d)//2
            col = (i - d)//2
            diffFlags[d] = True

            newPos = (row, col)

            if newPos in models:
                if models[newPos] == 'x':
                    newModels[newPos] = 'o'
                    point += 1
            else:
                newModels[newPos] = '+'
                point += 1

    return [point, newModels]


def getD(diffFlags, n, s):
    assert 2*n - s - 2>= 0

    r = min(s, 2*n-s - 2)
    assert s%2 == r%2

    for i in range(r, -1, -2):
        assert i >= 0

        if not diffFlags[i]:
            return i
        elif not diffFlags[-i]:
            return -i

    return None



t = int(input())
for i in range(t):
    n,m = map(int, input().split())

    models = {}
    for j in range(m):
        type, row, col = input().split()
        models[(int(row)-1, int(col)-1)] = type

    point, newModels = f(n, models)
    print('Case #' + str(i+1) + ':', point, len(newModels))

    for pos, type in newModels.items():
        print(type, pos[0]+1, pos[1]+1)



