#! /usr/bin/python

def solve(oper, where):
    otgt = []
    btgt = []
    for i in range(0,len(oper)):
        if oper[i]=='O':
            otgt.append(where[i])
        else:
            btgt.append(where[i])
    steps = 0
    idx_target = 0
    idx_otgt = 0
    idx_btgt = 0
    pos_o = 1
    pos_b = 1
    solved = False
    while not solved:
        if not solved:
            adv_target = False
            o_target = False
            b_target = False
            #orange robot
            if where[idx_target]==pos_o and oper[idx_target]=='O':
                adv_target = True
                o_target = True
            elif idx_otgt<len(otgt) and pos_o!=otgt[idx_otgt]:
                pos_o = pos_o + (1 if pos_o<otgt[idx_otgt] else -1)
            #blue robot
            if where[idx_target]==pos_b and oper[idx_target]=='B':
                adv_target = True
                b_target = True
            elif idx_btgt<len(btgt) and pos_b!=btgt[idx_btgt]:
                pos_b = pos_b + (1 if pos_b<btgt[idx_btgt] else -1)
            if adv_target:
                if idx_target==len(oper)-1:
                    solved = True
                if o_target:
                    idx_otgt = idx_otgt +1
                elif b_target:
                    idx_btgt = idx_btgt +1
                idx_target = idx_target +1
            steps = steps + 1
    return steps

if __name__ == "__main__":
    f = open("data.in","r")
    g = open("data.out","w")
    cases = int(f.readline().split()[0])
    for case in range(1,cases+1):
        line = f.readline().split()
        num = int(line[0])
        oper = []
        where = []
        idx = 1
        for i in range(1,num+1):
            oper.append(line[idx])
            where.append(int(line[idx+1]))
            idx = idx + 2
        steps = solve(oper,where)
        g.write("Case #%d: %d\n" % (case,steps))
    f.close()
    g.close()