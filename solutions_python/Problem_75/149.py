T = input()

for case in range(T):
    L = raw_input().split()

    C = int(L.pop(0))
    com = {}
    for _ in range(C):
        tmp = L.pop(0)
        com[tmp[:2]] = tmp[2]
        com[tmp[1::-1]] = tmp[2]

    D = int(L.pop(0))
    opp = {'Q':[],'W':[],'E':[],'R':[],'A':[],'S':[],'D':[],'F':[],}
    for _ in range(D):
        tmp = L.pop(0)
        opp[tmp[0]].append(tmp[1])
        opp[tmp[1]].append(tmp[0])

    inv = L[1]

    el = []
    oppel = set()
    for b in inv:
        if len(el) > 0 and (b+el[-1]) in com:
            el[-1] = com[b+el[-1]]
        else: 
            if len(el)>0 and el[-1] in opp:
                for x in opp[el[-1]]:
                    oppel.add(x)

            if b in oppel:
                el = []
                oppel = set()
            else:
                el.append(b)


                    

    if len(el) > 0:
        ans = reduce(lambda x,y: x + ', ' + y, el)
    else: 
        ans = ''
    ans = '[' + ans + ']'
    print "Case #%i:" % (case + 1), ans
