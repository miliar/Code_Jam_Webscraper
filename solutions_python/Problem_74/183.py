import sys

def solve_test(test):
    numbuttons = int(test[0])
    buttons = []
    for i in range(numbuttons):
        buttons.append((test[2*i+1], int(test[2*i+2])))
    steps = 0
    while buttons:
        opressed = move('O', buttons)
        bpressed = move('B', buttons)
        if opressed or bpressed:
            buttons = buttons[1:]
        steps += 1
    return steps

def move(color, buttonlist):
    next_buttons = filter(lambda x: x[0] == color, buttonlist)
    if not next_buttons:
        #print color, 'no buttons'
        return False # just wait
    else:
        next_button_num = next_buttons[0][1]
    if next_button_num > pos[color]:
        #print color, 'moved up', pos[color]+1
        pos[color] += 1
        return False
    elif next_button_num < pos[color]:
        #print color, 'moved down', pos[color]-1
        pos[color] -= 1
        return False
    elif buttonlist[0][0] == color:
        #print color, 'pressing button', pos[color]
        return True
    else:
        #print color, 'staying still', pos[color]
        return False

sequence = sys.stdin.readlines()
pos = {'O': 1, 'B': 1}

numtests = int(sequence[0])
for i in range(numtests):
    pos = {'O': 1, 'B': 1}
    print "Case #%d: %d" % (i+1,solve_test(sequence[i+1].split()))


