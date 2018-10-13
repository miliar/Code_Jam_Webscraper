#!/usr/bin/python
n = int(input())
for cases in range(n):
    inputString = raw_input()
    inputString = inputString.split(' ')

    n = inputString[0]
    n = int(n)
    inputString.pop(0)


    robot_O=[]
    robot_B=[]
    for i in range(n):
        robot = inputString[i*2] 
        goal  = int( inputString[i*2+1] )
        
        if robot == 'O':
            robot_O+= [{'index':i,'goal':goal}]
        else:
            robot_B+= [{'index':i,'goal':goal}]
            
    time = 0
    point_O=0;
    point_B=0;
    now_O=1;
    now_B=1;

    for i in range(n):

        if point_O!=len(robot_O) and robot_O[point_O]['index'] == i:
            move = abs( robot_O[point_O]['goal'] - now_O ) +1
            time+=move
            now_O = robot_O[point_O]['goal']
            if point_B!=len(robot_B):
                new_loc =  max( abs(robot_B[point_B]['goal']-now_B)-move, 0)
                now_B = robot_B[point_B]['goal'] + new_loc
            point_O+=1
        
        # point_B ==i
        else:
            move = abs( robot_B[point_B]['goal'] - now_B ) +1
            time+=move
            now_B = robot_B[point_B]['goal']
            if point_O!=len(robot_O):
                new_loc =  max( abs(robot_O[point_O]['goal']-now_O)-move, 0)
                now_O = robot_O[point_O]['goal'] + new_loc
            point_B+=1

#        print str(i) + ' ' + str(point_O) + ' ' + str(point_B)
#        print 'time:'+str(time)+' move:'+str(move)+' nowB:'+str(now_B)

    print 'Case #%(cases)d: %(time)d' % {'cases':cases+1, 'time':time}

