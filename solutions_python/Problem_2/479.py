f = open('large.in', 'r')
number_of_cases = int(f.readline())

count = 0

    
for i in xrange (0, number_of_cases):
    a_starts = []
    a_ends = []
    b_starts = []
    b_ends = []
    count += 1
    turn_time = int(f.readline())
    cases = f.readline()
    a_cases, b_cases = cases.split(' ')
    a_cases = int(a_cases)
    b_cases = int(b_cases)

    for j in xrange(0, a_cases):
        temp = f.readline()
        temp = temp.split(' ')
        st = temp[0].split(':')
        st = (int(st[0]) * 60 + int(st[1]))
        #print str(st)
        end = temp[1].split(':')
        end = (int(end[0]) * 60 + int(end[1]))
        #print str(end)
        a_starts.append(st)
        a_ends.append(end)
    a_starts.sort()
    a_ends.sort()
    for j in xrange(0, b_cases):
        temp = f.readline()
        temp = temp.split(' ')
        st = temp[0].split(':')
        st = (int(st[0]) * 60 + int(st[1]))
        #print st
        end = temp[1].split(':')
        end = (int(end[0]) * 60 + int(end[1]))
        #print end
        b_starts.append(st)
        b_ends.append(end)
    b_starts.sort()
    b_ends.sort()
    t_at_a = 0
    t_at_b = 0
    total_trains_used = 0
    trains_from_a = 0
    trains_from_b = 0

    while (len(b_starts) > 0 or len(a_starts) > 0):
        popped_time = 0
        pop = ''
        if (len(b_starts) > 0):
            if (len(a_starts) > 0):
                if (a_starts[0] < b_starts[0]):
                    popped_time = a_starts[0]
                    a_starts = a_starts[1:]
                    pop = 'a'
                else:
                    popped_time = b_starts[0]
                    b_starts = b_starts[1:]
                    pop = 'b'
            else:
                popped_time = b_starts[0]
                b_starts = b_starts[1:]
                pop = 'b'
        else:
            popped_time = a_starts[0]
            a_starts = a_starts[1:]
            pop = 'a'
        #print "Popped: " + str(popped_time)
        #if (len(a_ends) > 0):
            #print "First end: " + str(a_ends[0])
        if (len(a_ends) > 0):
            while ((a_ends[0] + turn_time) <= popped_time):
                t_at_b += 1
                a_ends = a_ends[1:]
                if (len(a_ends) == 0):
                    break;
        if (len(b_ends) > 0):
            while ((b_ends[0] + turn_time) <= popped_time):
                t_at_a += 1
                b_ends = b_ends[1:]
                if (len(b_ends) == 0):
                    break;
        #print "Trains at a: " + str(t_at_a)
        #print "Trains at b: " + str(t_at_b)

        if (pop == 'a'):
            if (t_at_a == 0):
                trains_from_a += 1
            else:
                t_at_a -= 1
        if (pop == 'b'):
            if (t_at_b == 0):
                trains_from_b += 1
            else:
                t_at_b -= 1
    print "Case #" + str(count) + ": " + str(trains_from_a) + " " + str(trains_from_b)
            


#print a_starts
#print a_ends
#print b_starts
#print b_ends
