
def solv(m):
    for i in range(len(m)):
        firstC = '?'
        currentC = '?'
        for j in range(len(m[0])):
            if m[i][j] != "?":
                if firstC == '?':
                    firstC = m[i][j]
                currentC = m[i][j]
            else:
                if currentC != '?':
                    m[i][j] = currentC
        j = 0
        while j < len(m[0]) and m[i][j] == "?":
            m[i][j] = firstC
            j+=1
    # print m
    for j in range(len(m[0])):
        firstC = '?'
        currentC = '?'
        for i in range(len(m)):
            if m[i][j] != "?":
                if firstC == '?':
                    firstC = m[i][j]
                currentC = m[i][j]
            else:
                if currentC != '?':
                    m[i][j] = currentC
        i = 0
        while i < len(m) and m[i][j] == '?':
            m[i][j] = firstC
            i += 1
    return m

def proc(ms):
    rtn = []
    for s in ms:
        row = reduce(lambda x, y: x+[y], s, [])
        rtn.append(row)
    return rtn

def main():
    n = int(raw_input())
    for i in range(n):
        x, y = map(int, raw_input().split(' '))
        data = []
        for j in range(x):
            data.append(raw_input())
        ans = solv(proc(data))
        print "Case #%d:" %(i+1)
        for j in range(x):
            print reduce(lambda a, b: a+b, ans[j], '')

if __name__ == "__main__":
    main()