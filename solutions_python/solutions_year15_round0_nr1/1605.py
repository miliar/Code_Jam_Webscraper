__author__ = 'Victor'

fi = open('A-large.in', 'r')
fo = open('StandingOvation.out', 'w')

t = int(next(fi))

for i in range(t):
    case = next(fi).strip().split()
    smax = case[0]
    public = [int(x) for x in list(case[1])]
    friends = 0
    people_clapping = 0

    for j in range(len(public)):
        if people_clapping >= j:
            people_clapping += public[j]
        else:
            need = j-people_clapping
            friends += need
            people_clapping += need
            people_clapping += public[j]

    fo.write('Case #%d: ' %(i+1))
    fo.write('%d' % friends)
    fo.write('\n')

fi.close()
fo.close()