#encoding: utf-8

debug = False

# File reading
input = open('A-large.in')

# Counting test cases
testn = int(input.readline())
i = 0

# Utilities

# First instruction for a robot
def find_first(instructions, robot):
    for i,(r,b) in enumerate(instructions):
        if r == robot : return i
    return -1

# Time to press
def ttp(instruction, pos):
    button = instruction[1]
    robot = instruction[0]
    position = pos[robot]
    return abs(button - position) + 1

# For each test case
while(i < testn):
    # Process instructions
    t = input.readline()[:-1].split(' ')[1:]
    t = zip(t[::2], t[1::2])
    t = [(r,int(b)) for r,b in t]

    # Simulate process
    min_time = 0
    pos = {'O' : 1, 'B' : 1}

    while len(t) > 0 :
        if debug :
            print '---------------'
            print t
            print pos
        fir = {'O' : find_first(t, 'O'),
               'B' : find_first(t, 'B')}

        if fir['O'] == -1 or fir['B'] == -1 :
            for inst in t:
                r,b = inst
                min_time += ttp(inst, pos)
                pos[r] = b
            if debug :
                print min_time
            break


        f_robot,f_button = t[min(fir['O'], fir['B'])]
        s_robot = 'O' if f_robot == 'B' else 'B'
        s_button = t[fir[s_robot]][1]

        ttps = {'O' : ttp(t[fir['O']], pos),
                'B' : ttp(t[fir['B']], pos)}

        pos[f_robot] = f_button
        if(ttps[s_robot] - ttps[f_robot] > 1):
            pos[s_robot] = pos[s_robot] + (1 if pos[s_robot] < s_button else -1) * ttps[f_robot]
        else:
            pos[s_robot] = s_button

        min_time += ttps[f_robot]
        del t[fir[f_robot]]
        if debug :
            print pos
            print t
            print min_time


    # Print result
    print "Case #%d: %d" % (i + 1, min_time)
    i += 1
