
def solve(array, r, c):
    l = 0
    mem = {}
    n = 0
    for i in range(r):
        for j in range(c):
            if array[i][j] != '?':
                mem[n] = (i, j)
                n += 1
    for i in range(n):
        x = mem[l][0]
        y = mem[i][1]
        l += 1
        j = 0
        if j  < r:
            while array[j][y] != array[x][y]:
                if array[j][y] == '?':
                    array[j][y] = array[x][y]
                j += 1
                if j  == r:
                    break
            j += 1
        if j  < r:
            while array[j][y] == '?':
                array[j][y] = array[x][y]
                j += 1
                if j  == r:
                    break
    return array

def solve2(array, r, c):
    l = 0
    mem = {}
    n = 0
    for i in range(r):
        for j in range(c):
            if array[i][j] != '?':
                mem[n] = (i, j)
                n += 1
    for i in range(n):
        x = mem[l][0]
        y = mem[i][1]
        l += 1
        j = 0
        if j  < c:
            while array[x][j] != array[x][y]:
                if array[x][j]  == '?':
                    array[x][j] = array[x][y]
                j += 1
                if j  == c:
                    break
            j += 1
        if j  < c:
            while array[x][j]  == '?':
                array[x][j] = array[x][y]
                j += 1
                if j  == c:
                    break
    return array






tests = int(input())

for test in range(tests):
    r, c = [int(x) for x in input().split()]
    array = [[0 for x in range(c)] for y in range(r)]
    mem = {}
    n = 0
    for i in range(r):
        s = input().split()
        for j in range(c):
            array[i][j] = s[0][j]
            if array[i][j] != '?':

                mem[n] = (i, j)
                n += 1
    res_array = solve(array, r, c)
    res_array2 = solve2(res_array, r, c)
    print("Case #%d:" % (test + 1))
    for i in range(len(res_array2)):
        print(''.join(res_array2[i]))