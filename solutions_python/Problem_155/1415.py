for t in xrange(int(raw_input())):
    m, shynesses = raw_input().split()
    i=0
    shyness = 0
    people_we_need = 0
    for num_peep_shyness in shynesses:
        people_we_need = max(people_we_need, shyness-i)
        i += int(num_peep_shyness)
        shyness += 1

    print 'Case #%d: %d' % (t+1, people_we_need)
