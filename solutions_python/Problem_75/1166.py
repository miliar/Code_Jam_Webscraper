T = int(raw_input())

for t in range(0,T):
    line = raw_input().split(' ')
    i = 0
    C = int(line[i])
    i+=1
    combos = {}
    for c in range(0,C):
        combos.update({line[i][:2] : line[i][2:]})
        i+=1
    bad = []
    D = int(line[i])
    i+=1
    for d in range(0,D):
        bad.append([line[i][0],line[i][1]])
        i+=1
    N = int(line[i])
    i+=1
    cast=[]
    for index in range(0,N):
        cast.append(line[i][index])
        tc = False
        for combo in combos.keys():
            if (combo[0] is combo[1]) and (cast[-2:].count(combo[1])>1):
                cast = cast[:-2]
                cast.append(combos[combo])
                tc = True
                break
            if (combo[0] is not combo[1]) and (combo[0] in cast[-2:]) and (combo[1] in cast[-2:]):
                cast = cast[:-2]
                cast.append(combos[combo])
                tc = True
                break
        if tc:
            continue
        for bd in bad:
            if (bd[0] is bd[1]) and cast.count(bd[0])>1:
                cast = []
                break
            elif (bd[0] is not bd[1]) and (bd[0] in cast) and (bd[1] in cast):
                cast = []
    print 'Case #' + str(t+1) + ': ' + str(cast).replace('\'','')
    