f = open('B-large.in')#'B-small-attempt0.in')#'test.in')#'A-large.in')
f_out = open('ProbB-large.out', 'w')
n = int(f.next())
test = 1
while test <= n:
    input_data = f.next().strip().split(' ')
    
    combs_num = int(input_data.pop(0))
    combs = []
    i = 0
    while i < combs_num:
        combs.append(input_data.pop(0))
        i += 1
    
    oppos_num = int(input_data.pop(0))
    oppos = []
    i = 0
    while i < oppos_num:
        oppos.append(input_data.pop(0))
        i += 1
    _ = input_data.pop(0)
    res = []
    for elem in input_data[0]:
        res.append(elem)
        if len(res) == 1:
            continue
        combo = False
        
        for comb in combs:
            if (res[len(res)-1] == comb[0] and res[len(res)-2] == comb[1]) or \
                    (res[len(res)-1] == comb[1] and res[len(res)-2] == comb[0]):
                res = res[:-2]
                res.append(comb[2])
                combo = True
                break
        if combo: continue
        for oppo in oppos:
            if oppo[0] in res and oppo[1] in res:
                res = []
                break
    f_out.write('Case #%d: %s\n' %(test, str(res).replace("'", '')))
    test += 1
