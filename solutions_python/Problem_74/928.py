from sys import argv

scrip, filename = argv

def read_file(filename):
    t = []
    fin = open(filename)
    cases = fin.readline()
    for line in fin:
        line = line.replace('O ', 'O')
        line = line.replace('B ', 'B')
        t.append(line[2:].split())
    fin.close()
    return t
    #for i in range(len(t)):
    #    t[i] = t[i].strip()
    #return t

def get_cases(t, in_no):
    res = []
    for i in range(1, len(t), in_no):
        tmp = []
        for k in range(in_no):
            tmp.append(t[i+k])
        res.append(tmp)
    return res

def write_output(res):
    fin = open('outputs.txt','w')
    for i in range(len(res)):
        fin.write("Case #%s: %s" %(i+1,res[i]))
        fin.write("\n")
    fin.close()


def compute_res1(cases):
    b_cp = 1
    o_cp = 1
    tt = 0
    olead = 0
    blead = 0
    last_time = 0
    last_robo = 1
    for case in cases:
        robo = case[0]
        if robo == 'O':
            tmp = do_o_case(o_cp, case[1:], olead)
            olead = 0
            blead += tmp[0]
            o_cp = tmp[1]
            tt += tmp[0]
        else:
            tmp = do_o_case(b_cp, case[1:], blead)
            blead = 0
            olead += tmp[0]
            b_cp = tmp[1]
            tt += tmp[0]
    return tt

def compute_res(cases):
    b_cp = 1
    o_cp = 1
    tt = 0
    olead = 0
    blead = 0
    last_time = 0
    last_robo = 1
    for case in cases:
        robo = case[0]
        if last_robo == 1:
            last_robo = robo
        if robo == 'O':
            tmp = do_o_case(o_cp, case[1:], olead)
            olead = 0
            if last_robo != robo:
                last_robo = 1
                if tmp[0] > last_time:
                    tt += tmp[0]
                    last_time = 0
                else:
                    tt += last_time + 1
                    last_time = 0
                olead = abs(last_time - tmp[0])
            else:
                last_time += tmp[0]
            o_cp = tmp[1]
        else:
            tmp = do_o_case(b_cp, case[1:], blead)
            blead = 0
            if last_robo != robo:
                last_robo = 1
                if tmp[0] > last_time:
                    tt += tmp[0]
                    last_time = 0
                else:
                    tt += last_time + 1
                    last_time = 0
                blead = abs(last_time - tmp[0])
            else:
                last_time += tmp[0]
            b_cp = tmp[1]
    if last_time > 0:
        tt += last_time
    return tt


            
def do_o_case(cp, dp, olead):
    res = 0
    diff = abs(int(dp)-cp)
    if olead > diff:
        res = 1
    else:
        res = (diff - olead) + 1 
    return [res, int(dp)]


#print compute_res(['B15', 'O15', 'B36', 'O37', 'O79', 'B81', 'B49', 'O46'])
#print compute_res1(['O2', 'B1', 'B2', 'O4'])
#print compute_res1(['O10', 'B10', 'O3', 'B1', 'O5', 'B6', 'O8', 'B7', 'O8', 'B9'])
#print compute_res1(['B32', 'O34', 'O55', 'B57', 'O24', 'B26', 'O38', 'B13', 'O82', 'B56'])
t = read_file(filename)
res = []
for item in t:
    res.append(compute_res1(item))
for i in range(len(t)):
    print t[i], "\n", res[i]
write_output(res)
#cases = get_cases(t, 3)
#res = compute_res(cases, res)
#print len(cases)
