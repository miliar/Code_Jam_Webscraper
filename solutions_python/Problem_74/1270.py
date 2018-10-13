in_file = open("sin.txt", "r")
out_file = open("sout.txt", "w")

test_cases = int(in_file.readline())
input_line = []

for test_case_count in range(1, test_cases+1):
    input_line = in_file.readline().split(' ')

    move_count = 0

    curr_robot_prev_button = 1
    prev_robot_prev_button = 1

    prev_robot = ''
    curr_delta = 0
    prev_delta = 0

    buttons_to_press = int(input_line.pop(0))

    for button_press_count in range(1, buttons_to_press+1):
        #button_press = in_file.readline()
        robot = input_line.pop(0)
        button = int(input_line.pop(0))
        #(robot, button) = button_press.split(' ')
    
        # If this is the first robot,
        # Set current delta move
        if len(prev_robot) == 0:
            move = button # as it is starting in position 1
            curr_robot_prev_button = button
            
            #print("Robot " + robot + " moves " + str(move) + " steps")
        
        # If same as prev robot
        # Add the move to delta
        elif robot == prev_robot:
            move = abs(curr_robot_prev_button - button)
            move = move + 1
            #move = move + curr_delta
            curr_robot_prev_button = button

            #print("Robot " + robot + " should move " + str(move) + " steps")

            if move <= prev_delta:
                #prev_delta = prev_delta - move
                move = 1
            else:
                move = move - prev_delta
                #prev_delta = 0

            #print("Robot " + robot + " moves " + str(move) + " steps")

        # If robot has changed
        elif robot != prev_robot:
            move = abs(prev_robot_prev_button - button)
            move = move + 1
            #move = move + prev_delta 

            #print("Robot " + robot + " should move " + str(move) + " steps")

            # interchange current and prev robot's prev buttons
            prev_robot_prev_button = curr_robot_prev_button
            curr_robot_prev_button = button

            # interchange delta
            prev_delta = curr_delta
            curr_delta = 0
            
            # calc delta
            if move <= prev_delta:
                #prev_delta = prev_delta - move
                move = 1
            else:
                move = move - prev_delta
                #prev_delta = 0

            #print("Robot " + robot + " moves " + str(move) + " steps")

        prev_delta = 0
        curr_delta = curr_delta + move
        #print("curr_delta = " + str(curr_delta))
        move_count = move_count + move
        #print("move_count = " + str(move_count))
        prev_robot = robot

    #move_count = move_count + curr_delta
    print("Case #" + str(test_case_count) + ": " + str(move_count), \
        file=out_file)

in_file.close()
out_file.close()
    
