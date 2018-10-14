import sys, os
##
##file_in = 'B-small-attempt1.in'
##file_out = 'B-small.out'
file_in = 'B-large.in'
file_out = 'B-large.out'
##file_in = 'test.txt'
##file_out = 'test.out.txt'

f = open(file_in, 'r')
res_f = open(file_out, 'w')

def add_min_to_time(min, time):
    add_h = int(min / 60)
    add_min = min % 60
    h = int(time[:2])
    m = int(time[-2:])
    m = m + add_min
    if m >= 60:
        m = m - 60
        h += 1
    h += add_h
    return '%02d:%02d' % (h,m)

def compute_number(turn_around, leave_a_list, leave_b_list):
    added_in_a = 0
    added_in_b = 0
    current_in_a = current_in_b = 0
    leave_a_list.sort()
    leave_b_list.sort()

    trains_to_arrive_in_a = []
    trains_to_arrive_in_b = []

    while leave_a_list or leave_b_list:

        if not leave_a_list:
            current_pos = 'B'
        elif not leave_b_list:
            current_pos = 'A'
        else:
            if leave_a_list[0] < leave_b_list[0]:
                current_pos = 'A'
            else:
                current_pos = 'B'

        if current_pos == 'A':
            dep, arr = leave_a_list[0]
            trains_to_arrive_in_a_bis = []
            trains_arrived = 0
            for t in trains_to_arrive_in_a:
                if t <= dep:
                    trains_arrived += 1
                else:
                    trains_to_arrive_in_a_bis.append(t)
            current_in_a += trains_arrived
            trains_to_arrive_in_a = trains_to_arrive_in_a_bis
            if current_in_a:
                current_in_a -= 1
            else:
                added_in_a += 1
            trains_to_arrive_in_b.append(arr)
            leave_a_list = leave_a_list[1:]
        else:
            dep, arr = leave_b_list[0]
            trains_to_arrive_in_b_bis = []
            trains_arrived = 0
            for t in trains_to_arrive_in_b:
                if t <= dep:
                    trains_arrived += 1
                else:
                    trains_to_arrive_in_b_bis.append(t)
            current_in_b += trains_arrived
            trains_to_arrive_in_b = trains_to_arrive_in_b_bis
            if current_in_b:
                current_in_b -= 1
            else:
                added_in_b += 1
            trains_to_arrive_in_a.append(arr)
            leave_b_list = leave_b_list[1:]

    return (added_in_a, added_in_b)


test_cases_num = 0

l = f.readline().strip('\n')
test_cases_num = int(l)
for i in range(test_cases_num):
    l = f.readline().strip('\n')
    turn_around = int(l)
    l = f.readline().strip('\n')
    na, nb = l.split()
    na = int(na)
    nb = int(nb)
    leave_a_list = []
    arrive_in_b_list = []
    leave_b_list = []
    arrive_in_a_list = []
    for j in range(na):
        l = f.readline().strip('\n')
        dep, arr = l.split()
        leave_a_list.append((dep, add_min_to_time(turn_around, arr)))
    for j in range(nb):
        l = f.readline().strip('\n')
        dep, arr = l.split()
        leave_b_list.append((dep,add_min_to_time(turn_around, arr)))


    froma, fromb = compute_number(turn_around, leave_a_list, leave_b_list)
    print >> res_f, "Case #%s: %s %s" % ((i+1), froma, fromb)


try:
    f.close()
    res_f.close()
except:
    pass

print "done"