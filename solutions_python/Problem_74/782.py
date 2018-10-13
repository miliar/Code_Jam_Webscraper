import os

input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

T = int(input.readline()) # Number of Trials

def solve_me(N, turn_list, blue_orders, orange_orders):
    turn_count = 0
    time = 1 # start 0 or 1?
    blue_pos = 1 # starting pos
    blue_step = 0 # what command are they on?
    orange_pos = 1
    orange_step = 0
    while True:
        next_turn = False
        # blue move
        if len(blue_orders) > 0 and blue_step < len(blue_orders):
            if blue_pos < int(blue_orders[blue_step]):
                blue_pos += 1
            elif blue_pos > int(blue_orders[blue_step]):
                blue_pos -= 1
            else: # on button, wait until turn to press
                if turn_list[turn_count] == "B":
                    # press button and update objective
                    next_turn = True
                    blue_step+=1
                # otherwise wait
        # orange move
        if len(orange_orders) > 0 and orange_step < len(orange_orders):
            if orange_pos < int(orange_orders[orange_step]):
                orange_pos += 1
            elif orange_pos > int(orange_orders[orange_step]):
                orange_pos -= 1
            else: # on button, wait until turn to press
                if turn_list[turn_count] == "O":
                    # press button and update objective
                    next_turn = True
                    orange_step+=1
                # otherwise wait
        # hustle the loop along
        if next_turn:
            turn_count+=1
        if turn_count == len(turn_list):
            # done!  exit
            return time
        else:
            time+=1

input_list = []
for t in xrange(T): # each test case
    turn_list = []
    blue_orders = []
    orange_orders = []
    line = input.readline()
    input_list = line.split()
    N = int(input_list[0])
    for i in xrange(N): # populate bot orders
        if input_list[2*i + 1] == "B":
            blue_orders.append(input_list[2*i+2])
        else:
            orange_orders.append(input_list[2*i+2])
        turn_list.append(input_list[2*i+1])  # so we know who's turn to push a button
    
    answer = solve_me(N, turn_list, blue_orders, orange_orders)
    output.write("Case #%d: %s"%(t+1, answer) + os.linesep)

output.close()
input.close()


