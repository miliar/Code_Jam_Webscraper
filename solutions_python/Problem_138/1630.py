fin = open("input.txt", 'r')
fout = open("output.txt", 'w')
t = int(fin.readline())


def calculate_common(naomi, ken):
    res = 0
    for i in range(len(naomi)):
        if naomi[i] > ken[i]:
            res += 1
    return res


for test in range(t):
    N = int(fin.readline())
    naomi_ = sorted(list(map(float, fin.readline().split())))
    ken_ = sorted(list(map(float, fin.readline().split())))
    naomi = naomi_.copy()
    ken = ken_.copy()
    # War Game
    points_war = 0
    while len(naomi) != 0:
        least = naomi[0]
        if max(ken) < least:
            ken.pop(0)
            points_war += 1
        else:
            i = 0
            while ken[i] < least:
                i += 1
            ken.pop(i)
        naomi.pop(0)
    #Deceitful War
    naomi = naomi_.copy()
    ken = ken_.copy()
    possible_points = []
    possible_points.append(calculate_common(naomi, ken))
    while len(naomi) != 0:
        least = naomi[0]
        if least < max(ken):
            ken.pop(len(ken) - 1)
            naomi.pop(0)
            possible_points.append(calculate_common(naomi, ken))
        else:
            break
    points_d_war = max(possible_points)
    fout.write("Case #" + str(test + 1) + ": " + str(points_d_war) + ' ' + str(points_war) + '\n')
fout.close()