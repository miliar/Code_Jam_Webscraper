T = int(input())
format_string = "Case #{0}: {1} {2}"

for i in range(T):
    N = int(input())
    naomi = [float(x) for x in input().strip().split()]
    ken = [float(x) for x in input().strip().split()]

    naomi.sort()
    ken.sort()

    ken_war = list(ken)
    naomi_war = list(naomi)
    war = 0

    while len(ken_war) > 0:
        if naomi_war[-1] > ken_war[-1]:
            naomi_war = naomi_war[:-1]
            ken_war = ken_war[1:]
            war += 1
        else:
            naomi_war = naomi_war[:-1]
            ken_war = ken_war[:-1]

    ken_deceitful = list(ken)
    naomi_deceitful = list(naomi)
    deceit = 0

    while len(ken_deceitful) > 0:
        if ken_deceitful[0] > naomi_deceitful[0]:
            naomi_deceitful = naomi_deceitful[1:]
            ken_deceitful = ken_deceitful[:-1]
        else:
            deceit += 1
            naomi_deceitful = naomi_deceitful[1:]
            ken_deceitful = ken_deceitful[1:]

    print(format_string.format(i+1, deceit, war))
