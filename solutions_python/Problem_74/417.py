def next(prev, robot):
    count = 1
    for button in sequence[robot][prev+1:]:
        if button != -1:
            return prev + count
        count = count + 1
    return -1

def move(pos, next_index, robot):
    
    global sequence
    if next_index == -1:
        return -1
    elif pos == sequence[robot][next_index]:
        return pos
    elif pos < sequence[robot][next_index]:
        return pos+1
    else:
        return pos-1
        
small_in = "A-large.in"
small_out = "A-large.out"

sequence = {'B': [], 'O': []}
output = ""
infile = open(small_in)
T = int(infile.readline().rstrip())
for i in range(T):
    data = infile.readline().rstrip().split()
    num = False
    N = int(data[0])
    sequence = {'B': [], 'O': []}
    for char in data[1:]:
        if not num:
            robot = char
        else:
            sequence[robot].append(int(char))
            if robot != 'B':
                sequence['B'].append(-1)
            else:
                sequence['O'].append(-1)
        num = not num
    print sequence
    #Solve
    button_pos = 0
    O_pos = 0
    B_pos = 0
    O_next = next(-1, 'O')
    B_next = next(-1, 'B')
    time = 0
    while True:
        O_valid = True
        B_valid = True
        if O_pos == sequence['O'][button_pos]:
            button_pos = button_pos + 1
            O_next = next(O_next, 'O')
            O_valid = False
        elif B_pos == sequence['B'][button_pos]:
            button_pos = button_pos + 1
            B_next = next(B_next, 'B')  
            B_valid = False
        if O_next != -1 and O_valid:
            O_pos = move(O_pos, O_next, 'O')
        if B_next != -1 and B_valid:
            B_pos = move(B_pos, B_next, 'B')
        if button_pos == len(sequence['O']):
            break;
        time = time + 1
    #Output
    output += "Case #" + str(i+1) + ": " + str(time) + "\n"

outfile = open(small_out, 'w')
outfile.write(output)
    
        