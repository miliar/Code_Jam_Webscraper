import sys

def make_state(old_state, new_position, robot_id):
    if (robot_id == 'B'): return (old_state[0], new_position)
    else: return (new_position, old_state[1])

def get_position(state, robot_id):
    if (robot_id == 'B'): return state[1]
    else: return state[0]    

def get_next_button(tc, robot_id):
    for (robot, pos) in tc:
        if (robot == robot_id):
            return pos
    return None

def solve_specific(current_position, tc, robot_id):
    next_button = get_next_button(tc, robot_id)

    # we're done, do nothing
    if (next_button == None): return (current_position, False)

    if (current_position > next_button):
#        print "Moving %s to button %d" % (robot_id, current_position -1)
        return (current_position - 1, False)
    elif (current_position < next_button):
#        print "Moving %s to button %d" % (robot_id, current_position +1)
        return (current_position + 1, False)
    elif (current_position == next_button and (tc[0][0] == robot_id)):
#        print "%s pushing button %d" % (robot_id, next_button)
        return (current_position, True)
    else:
#        print "%s staying at %d" % (robot_id, current_position)
        return (current_position, False)

def solve(state, tc):

    num_iters = 0

    while (len(tc) > 0):    
        (orange_pos, orange_pushed) = solve_specific(get_position(state, 'O'), tc, 'O')
        (blue_pos, blue_pushed) = solve_specific(get_position(state, 'B'), tc, 'B')    

        state = (orange_pos, blue_pos)
        if (orange_pushed and blue_pushed):
            print "bug!"
        
        if (orange_pushed or blue_pushed):
            tc = tc[1:]            

        num_iters += 1
        
    return num_iters
    
test_cases = []

f = open(sys.argv[1], "r")
output_name = sys.argv[1] + ".results"
output = open(output_name, "w+")

num_cases = int(f.readline())

for line in f.readlines():
    tc_raw = line.split(' ')
    num_items = int(tc_raw[0])
    tc = []
    for idx in range(0, num_items):
        tc.append ((tc_raw[2*idx + 1], int(tc_raw[2*idx + 2])))
    test_cases.append(tc)

# state = (ORANGE POSITION, BLUE POSITION)
initial_state = (1,1)

idx = 1
for tc in test_cases:
    print "Case #%d: %d" % (idx, solve(initial_state, tc))
    output.write("Case #%d: %d\n" % (idx, solve(initial_state, tc)))
    idx += 1

f.close()        