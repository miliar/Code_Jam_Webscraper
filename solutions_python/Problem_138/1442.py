INPUT_FILE = 'files/war_test.in'
OUTPUT_FILE = 'files/war_test.out'

in_file = open(INPUT_FILE, 'r')
out_file = open(OUTPUT_FILE, 'w')

n = int(in_file.readline())
case = 1

while n > 0:
    out_file.write('Case #' + str(case) + ': ')

    n_blocks = int(in_file.readline())
    naomi = sorted(map(float, in_file.readline().split()))
    ken = sorted(map(float, in_file.readline().split()))
    naomi_copy = list(naomi)
    ken_copy = list(ken)

    i = 0
    naomi_deceitful_score = 0
    while i < n_blocks:
        chosen_naomi = naomi.pop(0)
        if chosen_naomi < ken[0]:
            chosen_ken = ken.pop()
        else:
            chosen_ken = ken.pop(0)
        if chosen_naomi > chosen_ken:
            naomi_deceitful_score += 1
        i += 1

    i = 0
    naomi = naomi_copy
    ken = ken_copy
    naomi_war_score = 0
    while i < n_blocks:
        chosen_naomi = naomi.pop(0)
        chosen_ken = -1
        for index, k in enumerate(ken):
            if k > chosen_naomi:
                chosen_ken = ken.pop(index)
                break
        if chosen_ken == -1:
            ken.pop(0)
            naomi_war_score += 1
        i += 1

    out_file.write(str(naomi_deceitful_score) + ' ' + str(naomi_war_score) + '\n')

    n -= 1
    case += 1