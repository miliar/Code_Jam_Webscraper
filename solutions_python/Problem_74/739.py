f = open('A-large.in')#'A-small-attempt1.in')#'test.in')#'A-small-attempt0.in')#'test.in')
f_out = open('ProbA-large.out', 'w')
n = int(f.next())
test = 1
while test <= n:
    line = f.next().split(' ')
    _ = int(line.pop(0))
    res = 0
    o_act = 1
    b_act = 1
    o_path = []
    b_path = []
    order = []
    to_add = []
    for m in line:
        if m == 'O': 
            order.append('O')
            to_add = o_path
        elif m == 'B': 
            order.append('B')
            to_add = b_path
        else: to_add.append(int(m))
    while len(o_path) > 0 or len(b_path) > 0:
        who_free = None
        if len(o_path) > 0 and len(b_path) > 0:
            if o_act == o_path[0] and b_act == b_path[0]:
                if order[0] == 'B':
                    who_free = b_path
                else:
                    who_free = o_path
                #we will free him later
            elif o_act == o_path[0]:
                who_free = o_path
            elif b_act == b_path[0]:
                who_free = b_path
            
            if o_act < o_path[0]:
                o_act += 1
            elif o_act > o_path[0]:
                o_act -= 1
            
            if b_act < b_path[0]:
                b_act += 1
            elif b_act > b_path[0]:
                b_act -= 1
        elif len(o_path) > 0:
            if o_act == o_path[0]:
                who_free = o_path
            elif o_act < o_path[0]:
                o_act += 1
            elif o_act > o_path[0]:
                o_act -= 1
        elif len(b_path) > 0:
            if b_act == b_path[0]:
                who_free = b_path
            elif b_act < b_path[0]:
                b_act += 1
            elif b_act > b_path[0]:
                b_act -= 1
        if who_free is not None:
            if who_free == b_path and order[0] == 'B':
                order.pop(0)
                who_free.pop(0)
            elif who_free == o_path and order[0] == 'O':
                order.pop(0)
                who_free.pop(0)
        res +=1
    f_out.write('Case #%d: %d\n' %(test, res))
    test += 1
f.close()
f_out.close()
