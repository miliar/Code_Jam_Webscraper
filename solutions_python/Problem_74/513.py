def BOTTRUST():
    testcases = int(raw_input())
    for case in xrange(1,testcases+1):
        input = raw_input().split()
        buttons = int(input[0])
        orange = []
        blue = []
        sequence = []
        for i in xrange(0,buttons):
            color = input[1 + 2*i]
            sequence.append(color)
            if color == 'O':
                orange.append(int(input[1 + 2*i + 1]))
            elif color == 'B':
                blue.append(int(input[1 + 2*i + 1]))
        time = 0
        orange_left = len(orange)
        blue_left = len(blue)
        turn_index = 0
        blue_position = 1
        orange_position = 1
        blue_next = 0
        orange_next = 0
        while orange_left != 0 or blue_left != 0:
            time += 1
            turn = sequence[turn_index]
            #print 'Before proc:'
            #print locals()
            if turn == 'O':
                if orange_position == orange[orange_next]:
                   #Orange presses button
                    turn_index += 1
                    orange_left -= 1
                    if orange_next != len(orange)-1:
                        orange_next += 1
                elif orange[orange_next] > orange_position:
                    orange_position += 1
                else:
                    orange_position -= 1
                #Blue's possible moves
                if len(blue) != 0:
                    if blue[blue_next] > blue_position:
                        blue_position += 1
                    elif blue[blue_next] < blue_position:
                        blue_position -= 1
            else:
                if blue_position == blue[blue_next]:
                    #Blue presses button
                    turn_index += 1
                    blue_left -= 1
                    if blue_next != len(blue)-1:
                        blue_next += 1
                elif blue[blue_next] > blue_position:
                    blue_position += 1
                else:
                    blue_position -= 1
                #Orange's possible moves
                if len(orange) != 0:
                    if orange[orange_next] > orange_position:
                        orange_position += 1
                    elif orange[orange_next] < orange_position:
                        orange_position -= 1
            #print 'After proc:'
            #print locals()
        print 'Case #' + str(case) + ': ' + str(time)
        
BOTTRUST()
