import fileinput 

def find_lowest_two(inp):
    max_n = -1
    for i  in "RYB":
        if inp[i] > max_n:
            max_n = inp[i]
            max_c = i

    return [c for c in "RYB" if c != max_c]

def is_singleton(inp):
    for i in "RYBVGO":
        s = 0
        for j in "RYBVGO":
            if j != i:
                s += inp[j]
        if inp[i] > s:
            if s == 0 and inp[i] == 1:
                return True, i
    return False, 0


def is_impossible(inp):
    for i in "RYB":
        s = 0
        for j in "RYB":
            if j != i:
                s += inp[j]
        if inp[i] > s:
            return True
    return False

def find_max(inp, inp_set):
    m = -1
    for i in inp_set:
        if inp[i] > m:
            m_c = i
            m_n = inp[i]
    return m_c, m_n
    
def find_min(inp, inp_set):
    m = inp[inp_set[0]]
    m_c = inp_set[0]
    m_n = m
    for i in inp_set:
        if inp[i] < m:
            m_c = i
            m_n = inp[i]
    return m_c, m_n
            
def comp_val(a, b):
    return b[1] - a[1]

f = fileinput.input()
sets_num = int(f.readline())
for i in xrange(sets_num):
    print "Case #%d:" % (int(i) + 1),

    inp = {}
    N, inp["R"], inp["O"], inp["Y"], inp["G"], inp["B"], inp["V"] = [int(d) for d in f.readline().split(" ")]

    if is_singleton(inp)[0]:
        print is_singleton(inp)[1]
        continue

    l = []
    for j in "RYB":
        if j == "R":
            comp = "G"
        if j == "Y":
            comp = "V"
        if j == "B":
            comp = "O"
        obj = [j, inp[j] - inp[comp], comp, inp[comp]]

        l += [obj,]


    cont = False
    for obj in l:
        if obj[1] < 0:
            print "IMPOSSIBLE"
            cont = True
            break
        if obj[1] == 0 and obj[3] != 0:
            flag = False
            for z in l:
                if z[0] != obj[0]:
                    if z[1] != 0 or z[3] != 0:
                        print "IMPOSSIBLE"
                        cont = True
                        break
            if cont:
                break
            else:
                print (obj[0] + obj[2]) * obj[3]
                cont = True
                break
    if cont:
        continue

    l_2 = sorted(l, comp_val)
    l = sorted(l, comp_val)


    if l[0][1] > l[1][1] + l[2][1]:
        print "IMPOSSIBLE"
        continue

    out = ""

    rounds = l[1][1] - l[2][1]
    out += (l[0][0] + l[1][0]) * rounds

    l[0][1] -= rounds
    l[1][1] -= rounds

    k = (l[0][1] - l[1][1]) * 2
    out += (l[0][0] + l[1][0]) * (k / 2)
    out += (l[0][0] + l[2][0]) * (k / 2)
    
    l[0][1] -= k
    l[1][1] -= k / 2
    l[2][1] -= k / 2

    out += (l[0][0] + l[1][0] + l[2][0]) * l[0][1]

    for j in xrange(3):
        if l[j][3] != 0:
            out = out.replace(l[j][0], ((l[j][0] + l[j][2]) * l[j][3]) + l[j][0], 1)
            
    print out
    

    
        

    
    







