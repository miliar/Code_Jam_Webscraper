__author__ = 'user'

with open('A-large.in') as f:
    cases = f.readline()
    cases = int(cases)
    for i in xrange(1, cases+1):
        line = f.readline()
        in_data = line.split(' ')
        shyness = int(in_data[0])
        crowd = map(int, in_data[1][:-1])
        counter = 0
        add_friends = 0
        for shy in xrange(shyness+1):
            add_friends += max(0, shy - counter)
            counter = max(counter, shy) + crowd[shy]
        print 'Case #{i}: {res}'.format(res=add_friends, i=i)