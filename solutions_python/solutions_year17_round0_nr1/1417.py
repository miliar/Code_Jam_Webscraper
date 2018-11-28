def turn(pen):
    if pen =='+':
        pen = '-'
    else:
        pen = '+'
    return pen

t = int(input())
for r in range(t):
    q,m = input().split(' ')
    ql = list(q)
    count = 0
    tmp = -2
    index = 0
    jj = 0

    if '-' not in q:
        print("Case #%s: %s" % (r+1, count))
        continue

    while index <= len(ql) - int(m):
        if ql[index] == '-':
            # if (tmp == index):
            #     break;
            for c in range(int(m)):
                ql[index + c] = turn(ql[index + c])
                tmp = index
                # index = 0
            count+=1
        else:
            index += 1
    result = "".join(ql)
    if '-' not in result:
        print("Case #%s: %s" % (r + 1, count))
    else:
        print("Case #%s: %s" % (r + 1, 'IMPOSSIBLE'))
