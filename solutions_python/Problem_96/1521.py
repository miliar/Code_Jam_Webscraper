import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()[1:]
f.close()

case = 1
for line in lines:
    tok = line.split()
    numdancers = int(tok[0])
    surprise = int(tok[1])
    maxscore = int(tok[2])
    scores = []
    count = 0

    for score in tok[3:]:
        i = int(score)
        f = int(i/3)
        s = f
        t = i - f*2
        scores.append([f, s, t])

    for iscore in scores:
        if max(iscore) - min(iscore) == 2:
            iscore[iscore.index(max(iscore))] -= 1
            iscore[iscore.index(min(iscore))] += 1

    for iscore in scores:
        if max(iscore) > 10:
            iscore[iscore.index(max(iscore))] -= 1
            iscore[iscore.index(min(iscore))] += 1

    for iscores in scores:
        if max(iscores) < maxscore and max(iscores) + 1 >= maxscore and surprise > 0:
            if max(iscores) - min(iscores) == 0:
                if max(iscores) < 10 and min(iscores) > 0:
                    iscores[iscores.index(max(iscores))] += 1
                    iscores[iscores.index(min(iscores))] -= 1
                    surprise -= 1
            elif max(iscores) - min(iscores) == 1:
                ma = max(iscores)
                mi = min(iscores)
                if iscores.count(ma) == 2:
                    iscores[iscores.index(mi)] += 2
                    iscores[iscores.index(ma)] -= 1
                    iscores[iscores.index(ma)] -= 1
                    surprise -= 1
                else:
                    iscores[iscores.index(ma)] -= 2
                    iscores[iscores.index(mi)] -= 1
                    iscores[iscores.index(mi)] -= 1
                    surprise -= 1

    for iscore in scores:
        if max(iscore) >= maxscore:
            count += 1
    
    print 'Case #' + str(case) + ': ' + str(count)
    case += 1
