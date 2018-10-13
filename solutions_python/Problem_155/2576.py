def test_audience(audience):
    amount_standing = 0
    for p, people in enumerate(audience):
        for i in range(people):
            if p <= amount_standing:
                amount_standing += 1
            else:
               return False 
    return sum(audience) == amount_standing

with(open('in-large.txt')) as file:
    cases = {}
    for i,l in enumerate(file.read().splitlines()):
        if i == 0:
            continue
        audience = [int(p) for p in l.split(' ')[1]]
        cases[i] = audience 

    for c, case in cases.iteritems():
        all_standing = False
        additional_friends = 0
        audience = case[:]
        while not all_standing:
            if not test_audience(audience):
                audience[0] += 1
                additional_friends += 1
            else:
                all_standing = True
        print "Case #%d: %d" % (c, additional_friends)
