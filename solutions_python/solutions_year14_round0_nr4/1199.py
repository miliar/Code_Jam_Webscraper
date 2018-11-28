def war(naomi, ken):
    count = 0
    while len(naomi) > 0:
        n_pick = naomi.pop()
        k_pick = len(ken) - 1
        for i in range(0, len(ken)):
            if ken[i] > n_pick:
                k_pick = i
        k_pick = ken.pop(k_pick)
        if n_pick > k_pick:
            count += 1
    return count

def deceitful_war(naomi, ken):
    scores = []
    while len(naomi) > 0:
        count = 0
        for i in range(0, len(naomi)):
            if (naomi[i] > ken[i]):
                count += 1
        scores.append(count)
        naomi.pop()
        ken.pop(0)
    return max(scores)

t = int(raw_input())
for i in range(1, t+1):
    raw_input() #don't care about count
    line = raw_input().split(" ")
    naomi = [float(x) for x in line]
    line = raw_input().split(" ")
    ken = [float(x) for x in line]
    ken.sort()
    ken.reverse()
    d_naomi = list(naomi)
    d_naomi.sort()
    d_naomi.reverse()
    d_ken = list(ken)
    print "Case #" + str(i) + ": " + str(deceitful_war(d_naomi, d_ken)) + " " + str(war(naomi, ken))
