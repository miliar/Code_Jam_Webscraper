import math

cases_number = int(raw_input())
test_cases = []
for i in range(cases_number):
    test_cases.append(raw_input())

def total(holes):
    my_sum = 0
    for each in holes.values():
        my_sum += each
    return my_sum

def max_hole(holes):
    my_max = 0
    for hole_size, hole_number in holes.iteritems():
        if (hole_size > my_max) & (hole_number > 0):
            my_max = hole_size
    return my_max

def delete_val(size, holes):
    for key, value in holes.iteritems():
        if key == size:
            holes[key] = 0
            return value



for i in range(cases_number):
    get_input = test_cases[i].split()
    stalls = int(get_input[0])
    people = int(get_input[1])
    holes = {stalls:1} #1000:1

    while total(holes) < people+1:
        max_hole_size = max_hole(holes)
        right_side = int(math.ceil((max_hole_size-1)/2.0))
        left_side = (max_hole_size-1)/2
        displaced = holes[max_hole_size]
        holes[max_hole_size] = 0
        holes[left_side] = holes.get(left_side, 0) + displaced
        holes[right_side] = holes.get(right_side, 0) + displaced


    print "Case #" + str(i+1) + ": " + str(right_side) + " " + str(left_side)
