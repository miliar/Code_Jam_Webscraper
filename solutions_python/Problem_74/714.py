n = int(raw_input(''))


def split_o_b(m):
    b_list = []
    o_list = []
    for i in range(int(m[0])):
        if m[2*i+1] == 'B':
            b_list.append(int(m[2*i+2]))
        elif m[2*i+1] == 'O':
            o_list.append(int(m[2*i+2]))
    return o_list, b_list
# input  2 4 5 2 9 100 ...
# output M P M M P M P ...
def make_schedule(move):
    now = 1
    out = []
    for j in move:
        m_num = abs(now-j)+1
        out.append(m_num)
        now = j
    return out

def merge(o, b, m):
    counter = 0
    o_stock = 0
    b_stock = 0

    for i in range(int(m[0])):
        if m[2*i+1] == 'B':
            if b_stock+1 > b[0]:
                counter = counter + 1
                o_stock = 1
                b_stock = 0
            else:
                counter = counter + b[0]-b_stock
                o_stock = o_stock + b[0]-b_stock
                b_stock = 0
            del b[0]
        elif m[2*i+1] == 'O':
            if o_stock +1 > o[0]:
                counter = counter + 1
                b_stock = 1
                o_stock = 0
            else:
                counter = counter + o[0]-o_stock
                b_stock = b_stock + o[0]-o_stock
                o_stock = 0
            del o[0]
    return counter
        

for i in range(n):
    move = raw_input('').split()
    #print move
    num = move[0]
    o_move, b_move = split_o_b(move)
    o_sche = make_schedule(o_move)
    b_sche = make_schedule(b_move)
    #print o_sche
    #print b_sche
    hoge = merge(o_sche, b_sche, move)
    print '''Case #%d: %d''' % (i+1, hoge)
    #print ''
