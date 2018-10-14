
question = open('./question.txt' , 'r')
answer = open('./answer.txt' , 'w')
#declare essential thing
robot_turn = []
button_to_push = []

#eat off the case number
case = question.readline()

case = 0
for lines in question:
    case += 1
    #declare essential thing
    robot_turn = []
    button_to_push = []
    time = 0;
    robot = [[],[]]
    position = [1,1]
    who_can_push_button_now = None

    #create a sequence of button that need to be pushed by robot
    sequence = lines.rstrip().split(" ")
    sequence.pop(0)
    for button in range(0 , len(sequence)-1, 2):
        robot_turn.append(sequence[button])
        button_to_push.append(int(sequence[button+1]))

    #create button-to-push sequence by particular robot
    for s in range(0 , len(button_to_push)):
        if robot_turn[s] == 'O':
            robot[0].append(button_to_push[s])
        else:
            robot[1].append(button_to_push[s])

    print robot_turn
    print robot
    
    for Pusher in robot_turn:
        button_pushed = False
        while not button_pushed:
            #convert pusher to numeric
            if Pusher == 'O':
                pusher_num = 0 ;
            else:
                pusher_num = 1 ;
            #4 condition for each robot ... push , ++ , -- , stay
            #time begin to tick
            time += 1

            if len(robot[pusher_num]) != 0:
                #someone get to move first .. namely pusher
                if robot[pusher_num][0] == position[pusher_num]:
                    print "Pushed!!"
                    robot[pusher_num].pop(0)
                    button_pushed = True
                elif robot[pusher_num][0] > position[pusher_num]:
                    position[pusher_num] += 1
                elif robot[pusher_num][0] < position[pusher_num]:
                    position[pusher_num] -= 1

            if len(robot[(pusher_num+1)%2]) != 0:
                #next robot move
                if robot[(pusher_num+1)%2][0] == position[(pusher_num+1)%2]:
                    print "stay"
                elif robot[(pusher_num+1)%2][0] > position[(pusher_num+1)%2]:
                    position[(pusher_num+1)%2] += 1
                elif robot[(pusher_num+1)%2][0] < position[(pusher_num+1)%2]:
                    position[(pusher_num+1)%2] -= 1

    answer.write("Case #"+str(case)+": "+str(time)+'\n')
    print "Case #"+str(case)+": "+str(time)
    del robot
    del robot_turn
    del button_to_push

question.close()
answer.close()
