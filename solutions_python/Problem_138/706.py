def deceitful_war(N, naomi, ken):
    pts = 0

    naomi.reverse()

    for i in range(N):
        if ken[0] < naomi[0]:
            pts += 1
            ken.pop(0)
            naomi.pop(0)
        elif ken[-1] > naomi[-1]:
            ken.pop()
            naomi.pop(0)
        else:
            for j in range(len(naomi)):
                if naomi[j] > ken[0]:
                    naomi.pop(j)
                    ken.pop(0)
                    pts += 1
                    break

    return pts

def war(N, naomi, ken):
    pts = 0
    naomi.reverse()

    worst = 0
    best = N - 1

    for i in range(N):
        if naomi[i] > ken[best]:
            worst += 1
            pts += 1
        else:
            best -= 1

    return pts

with open("D-large.in", "r") as f:
    with open("D-large.out", "w") as fo:
        line = f.readline()

        T = int(line.strip())

        for i in range(T):
            N = int(f.readline().strip())
            naomi = sorted(list(map(float, f.readline().strip().split())))
            ken = sorted(list(map(float, f.readline().strip().split())))
            
            war_score = war(N, naomi, ken)
            dwar_score = deceitful_war(N, naomi, ken)
            print("Case #%d: %d %d" % (i + 1, dwar_score, war_score))
            fo.write("Case #%d: %d %d\n" % (i + 1, dwar_score, war_score))
            