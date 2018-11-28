

tCases = int(raw_input())

for t in range(0, tCases):

    predata = raw_input().split(" ")

    data1 = predata[0]
    n = int(predata[1])

    data = [str(s) for s in data1]
    x = 0
    swapCnt = 0

    while x != len(data):

        if data[x] == '-':
            if x+n-1 < len(data):
                for each in range(x, x+n):
                    if data[each] == '-':
                        data[each] = '+'
                    elif data[each] == '+':
                        data[each] = '-'
            swapCnt += 1

        x += 1

    sorted_D = True
    for each in range(0, len(data)):
        if data[each] == '-':
            sorted_D = False

    if sorted_D:
        print 'Case #'+str(t+1)+': '+str(swapCnt)
    else:
        print 'Case #'+str(t+1)+': IMPOSSIBLE'
