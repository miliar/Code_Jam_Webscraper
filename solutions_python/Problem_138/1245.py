import random

file = open("war_sample.txt")
out = open('war_test.txt', 'w')
T = int(file.readline().strip())

case = 1
for cases in range(T):
    N_counter = 0
    Nd_counter = 0
    K_counter = 0
    Kd_counter = 0
    N = int(file.readline().strip())
    naomi_list = file.readline().split()
    ken_list = file.readline().split()
    a = sorted(naomi_list)
    b = sorted(ken_list)
    c = sorted(naomi_list)
    d = sorted(ken_list)
    for i in range(len(c)):
        if max(c) > max(d):
            N_counter += 1
            c.remove(c[-1])
            d.remove(d[0])
        else:
            K_counter += 1
            c.remove(c[-1])
            d.remove(d[-1])
    for j in range(len(b)):
        if max(b) > max(a):
            n_told_range = float(max(b)) - float(min(a))
            random_in_range = random.uniform(n_told_range, float(max(b)))
            while random_in_range in b:
                random_in_range = random.uniform(n_told_range, float(max(b)))
            n_told = random_in_range
            if float(max(b)) > n_told:
                Kd_counter += 1
            else:
                Nd_counter += 1
            a.remove(a[0])
            b.remove(b[-1])
        else:
            Nd_counter += 1
            a.remove(a[-1])
            b.remove(b[-1])

    out.write("Case #%i: %i %i\n" % (case, Nd_counter, N_counter))
    case += 1