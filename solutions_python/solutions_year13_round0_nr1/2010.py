lines = open('A-large.in').read().splitlines()
test_cases = int(lines[0])
start = 1
maps = lines[1:]
maps = filter(None, maps)
winning_x = [list("TXXX"), list("XXXX")]
winning_y = [list("OOOT"), list("OOOO")]
current_case = 0;
iterator = 0
second = 0
outcome = 0
while(current_case < test_cases):

    outcome = 0
    current_map = maps[(current_case*4):(current_case*4+4)]
    listed_map = [list(line) for line in current_map]
    for line in listed_map:
        if('.' in line):
            outcome = 3
    for row in listed_map:
        if(sorted(row) in winning_x):
            outcome = 1
        elif(sorted(row) in winning_y):
            outcome = 2
    zipped_map = zip(*listed_map)
    for row in zipped_map:
        if(sorted(row) in winning_x):
            outcome = 1
        elif(sorted(row) in winning_y):
            outcome = 2
    diagonal_one = [listed_map[i][i] for i in range(len(listed_map))]
    if(sorted(diagonal_one) in winning_x):
        outcome = 1
    elif(sorted(diagonal_one) in winning_y):
        outcome = 2

    diagonal_two = [listed_map[i][len(listed_map)-i-1] for i in range(len(listed_map))]
    if(sorted(diagonal_two) in winning_x):
        outcome = 1
    elif(sorted(diagonal_two) in winning_y):
        outcome = 2

    if('.' in listed_map):
        outcome = 3
        
    if(outcome == 1):
        print("Case #" + str(current_case+1) + ": X won")
    elif(outcome == 2):
        print("Case #" + str(current_case+1) + ": O won")
    elif(outcome == 3):
        print("Case #" + str(current_case+1) + ": Game has not completed")
    else:
        print("Case #" + str(current_case+1) + ": Draw")
    current_case += 1
