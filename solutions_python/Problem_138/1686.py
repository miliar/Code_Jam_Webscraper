import itertools

input = open("jamcode.txt")

T = int(input.readline())

def naomiNePeutPasBattreKen(naomi, ken):
    while (len(naomi) > 0 and min(naomi) > min(ken)):
        naomi.remove(min(naomi))
        ken.remove(min(ken))
    if (len(naomi) == 0):
        return False
    return True

for i in range(T):
    N = int(input.readline())
    score_deceitful = N
    score_war = 0
    naomi = [float(x) for x in input.readline().split()]
    ken = [float(x) for x in input.readline().split()]
    naomi2 = list(naomi)
    ken2 = list(ken)
    while (naomiNePeutPasBattreKen(naomi, ken)):
        score_deceitful -= 1
        naomi.remove(min(naomi))
        ken.remove(max(ken))
    while (len(naomi2) > 0):
        prop_naomi = min(naomi2)
        prop_ken = min(ken2)
        for element in ken2:
            if (element > prop_naomi):
                if prop_ken > prop_naomi:
                    if element < prop_ken:
                        prop_ken = element
                else:
                    prop_ken = element
        naomi2.remove(prop_naomi)
        ken2.remove(prop_ken)
        if prop_naomi > prop_ken:
            score_war += 1
    print("Case #"+str(i+1)+": "+str(score_deceitful)+" "+str(score_war))
