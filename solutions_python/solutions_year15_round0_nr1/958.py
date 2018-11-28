T = int(raw_input())

for case in range(T):
    s_max, s_values = raw_input().split()
    s_values = list(s_values)

    def clap_depend():
        return [(lvl, sum([int(x) for x in s_values[:lvl]])) for lvl in range(int(s_max)+1)]

    def unsuff(l):
        return filter(lambda t: t[1] < t[0], l)

    add_persons = 0
    target = unsuff(clap_depend())
    while len(target):
        x = target.pop(0)
        diff = (x[0] - x[1])
        s_values[x[0]-1] = str(int(s_values[x[0]-1]) + diff)
        add_persons += diff
        target = unsuff(clap_depend())

    print "Case #%d: %d" % (case+1, add_persons)