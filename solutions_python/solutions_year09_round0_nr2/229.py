def mat2str(mat):
    ans = ''
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            ans += str(mat[x][y]) + ' '
        ans = ans.rstrip() + '\n'
    return ans

def getflow(col, row, input):
    d = dict([])
    if col > 0:
        d[0] = input[col - 1][row] #North
    if row > 0:
        d[1] = input[col][row - 1] #West
    if row < SIZE_ROW - 1:
        d[2] = input[col][row + 1] #East
    if col < SIZE_COL - 1:
        d[3] = input[col + 1][row] #South

    #sink
    minimum = min(d.values())
    #print d.values()
    if minimum >= input[col][row]:
        return 4
    else:
        ans = []
        for key in d:
            if d[key] == minimum:
                ans.append(key)
        return min(ans)
def getsink(col, row, flow):
    if flow[col][row] == 4:
        return (col, row)
    c, r = col, row
    if flow[col][row] == 0:
        c = col - 1
    elif flow[col][row] == 1:
        r = row - 1
    elif flow[col][row] == 2:
        r = row + 1
    elif flow[col][row] == 3:
        c = col + 1
    else:
        print 'error: getans'
        return
    return getsink(c, r, flow)

def getchar(col, row, flow, ans, ch):
    ans[col][row] = chr(ch)

    if col > 0 and flow[col - 1][row] == 3:
        getchar(col - 1, row, flow, ans, ch)
    if row > 0 and flow[col][row - 1] == 2:
        getchar(col, row - 1, flow, ans, ch)
    if row < SIZE_ROW - 1 and flow[col][row + 1] == 1:
        getchar(col, row + 1, flow, ans, ch)
    if col < SIZE_COL - 1 and flow[col + 1][row] == 0:
        getchar(col + 1, row, flow, ans, ch)


def B(input):
    input = [[int(_x) for _x in seq.split()] for seq in input]
    SIZE_COL, SIZE_ROW = len(input), len(input[0])

    if SIZE_COL == SIZE_ROW == 1:
        return 'a'

    flow = [ [None] * SIZE_ROW for col in range(SIZE_COL)]
    ans = [ [None] * SIZE_ROW for col in range(SIZE_COL)]
    for col in range(SIZE_COL):
        for row in range(SIZE_ROW):
            #flow[col][row] = getflow(col, row)
            flow[col][row] = getflow(col, row, input)
            #print flow

    ch = ord('a')
    for col in range(SIZE_COL):
        for row in range(SIZE_ROW):
            if ans[col][row] == None:
                sink = getsink(col, row, flow)
                getchar(sink[0], sink[1], flow, ans, ch)
                #print ans
                ch += 1

    return ans
    #print flow
    #return flow

if __name__ == '__main__':
    #str_in = 'B-small-attempt1.in'
    str_in = 'B-large.in'
    f_in = open(str_in)
    f_out = open(str_in.rstrip('.in') + '.out', 'w')

    f_in.next()
    num_q = 1
    try:
        while True:
            SIZE_COL, SIZE_ROW = [int(_s) for _s in f_in.next().strip().split()]
            input = []
            for col in range(SIZE_COL):
                input.append(f_in.next().strip())
            #f_out.write('Case #' + str(num_q) + ': ' + B(input) + '\n')
            f_out.write('Case #' + str(num_q) + ': \n' + mat2str(B(input)) + '\n')
            #print num_q, input
            num_q += 1
            #print num_q

    except StopIteration:
        #print 'File Read Exit'
        pass

    f_in.close(); f_out.close()
    #print A_D, set_A
