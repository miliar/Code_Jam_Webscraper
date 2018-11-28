def to_n(fl):
    no0 = []
    flag = False
    for e in fl:
        if flag or e != 0:
            flag = True
            no0.append(e)
            
    return "".join([str(i) for i in no0])
            
        

def fix(l, last_i):
    if last_i == len(l) - 1:
        return l
    return l[:last_i] + [l[last_i] - 1] + [9] * (len(l) - last_i - 1)
  
def last(l):
    if len(l) == 1:
        return -1
    old = l[-1]
    jli = [j for j in range(0, len(l) - 1)]
    last_i = len(l) - 1
    for i in jli[::-1]:
        if l[i] <= old:
            old = l[i]
        else:
            old = l[i] - 1
            last_i = i
    return last_i
        




res = []
with open("B-large.in") as f:
    t = int(f.readline().strip())
    print t
    cont = 0
    for r in range(t):
        n = f.readline().strip()
        print cont
        cont += 1
        print n
        my_l = [int(i) for i in list(n)]
        # print my_l
        my_last = last(my_l)
        # print my_last
        if my_last >= 0:
            # print fix(my_l, last(my_l))
            # print to_n(fix(my_l, last(my_l)))
            res.append(to_n(fix(my_l, last(my_l))))
        else:
            # print n
            res.append(n)
        print "\t" + res[-1]
        
        # print n, to_n(fix(my_l, last(my_l)))
        # res.append(solve(comb, n))
        
with open("outbLarge.txt", "w") as out:
    for i, r in enumerate(res):
        out.write("Case #{}: {}\n".format(i+1, str(r) if r > -1 else "IMPOSSIBLE"))
