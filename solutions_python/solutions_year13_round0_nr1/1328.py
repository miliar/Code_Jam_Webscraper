#!/bin/env python

def check(data, cur_x, cur_y, interval_x, interval_y):
    x_count = 0
    o_count = 0
    t_count = 0
    #print "(%d, %d, %d, %d)" % (cur_x, cur_y, interval_x, interval_y)
    for n in range(4):
        val = data[cur_x][cur_y]
        if val == 'X':
            x_count += 1
        elif val == 'O':
            o_count +=1
        elif val == 'T':
            t_count +=1
        cur_x += interval_x
        cur_y += interval_y
    #print "X : %d, O : %d, T : %d" % (x_count, o_count, t_count)
    if x_count + t_count == 4:
        return 'X'
    elif o_count + t_count == 4:
        return 'O'
    else:
        return None

def solve(data):
    for x in range(4):
        y = 0
        if x == 0:
            ret = check(data, x, y, 1, 0) # row check
            if ret != None:
                return ret
            ret = check(data, x, y, 1, 1) # diagonal check
            if ret != None:
                return ret
        ret = check(data, x, y, 0, 1)
        if ret != None:
            return ret

        if x == 3:
            ret = check(data, x, y, -1, 1)
            if ret != None:
                return ret

    for y in range(1, 4):
        x = 0
        ret = check(data, x, y, 1, 0) # row check
        if ret != None:
            return ret

tc = int(raw_input())

for n in range(tc):
    data = []
    for i in range(4):
        line = raw_input()
        data.append(list(line))
    result = solve(data)    
    print "Case #%d:" % (n + 1),
    if result == "X":
        print "X won"
    elif result == "O":
        print "O won"
    else:
        flag = True
        for i in data:
            if flag:
                for j in i:
                    if j == '.':
                        flag = False
                        print "Game has not completed"
                        break
        if flag:
            print "Draw"
    try:
        raw_input()
    except:
        pass
