def standing_ovation_case_n(smax, people=''):
    count = 0
    invite = 0
    for i in range(0, int(smax)+1):
        n = int(people[i])
        if i > count:
            invite += 1
            count += 1
        count += n
    return invite

def standing_ovation(T, cases):
    for i in range(0,T):
        print "Case #%i: %i" % (i+1, standing_ovation_case_n(cases[i][0], cases[i][1]))

T = input()
cases = []
for i in range(0, T):
    cases.append(raw_input().split())

standing_ovation(T, cases)


