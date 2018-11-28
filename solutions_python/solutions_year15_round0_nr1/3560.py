n_tests = int(raw_input())
test = 0
while test<n_tests:
    test = test + 1
    a = raw_input()
    b = a.split(' ')
    smax = int(b[0])
    needed = 0
    l_needed = 0
    slvl = 0
    total_people = 0
    for s in b[1]:
        people = int(s)
        if people > 0:
            l_needed = slvl - total_people
        if l_needed > needed:
		    needed = l_needed
        if total_people >= smax:
            break
        total_people = total_people + people
        
        slvl = slvl + 1
    if needed < 0:
        needed = 0
    print 'Case #%s:' % test, needed,
    if test<n_tests:
        print ''