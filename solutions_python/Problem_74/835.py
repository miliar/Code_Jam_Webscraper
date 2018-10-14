# Problem A. Bot Trust

current = -1

with open('input.txt') as a_file:

    for a_problemset in a_file: # Case #current : turn

        current += 1

        if current == 0: # 문제 수를 구하기 위해 딱 한번 실행. 사실 필요없음.
            number_of_problem = a_problemset.strip()
            continue
        
        problem = a_problemset.split()

        number_of_set = problem[0] # 세트 수

        del problem[0] # 로봇과 버튼을 분리 한다

        O = [] # 0
        B = [] # 1
        switch = 0
        waitfor = [] # 로봇 순서

        for item in problem:

            if item == 'O': # 로봇 식별
                switch = 0
                waitfor.insert(0,item)
            elif item == 'B':
                switch = 1
                waitfor.insert(0,item)
            else:
                if switch == 0: # 로봇별 버튼 식별
                    O.insert(0,item)
                elif switch == 1:
                    B.insert(0,item)
            
        turn = 0 # 답을 구한다
        O_foot = 1
        B_foot = 1
        robot = None
        goal_O = None
        goal_B = None

        while 1:

            turn += 1

            if not robot:
                if waitfor:
                    robot = waitfor.pop()
            if not goal_O:
                if O:
                    goal_O = int(O.pop())
            if not goal_B:
                if B:
                    goal_B = int(B.pop())

            #orange robot turn
            if goal_O:
                if goal_O == O_foot:
                    if robot == 'O': # push button
                        goal_O = None
                        robot = None
                        print('Orange push button')
                    #else: stay
                else: # walk
                    if goal_O > O_foot:
                        O_foot += 1 # go
                    else : O_foot -= 1 # back

            #blue robot turn
            if goal_B:
                if goal_B == B_foot:
                    if robot == 'B': # push button
                        goal_B = None
                        robot = None
                        print('Blue push button')
                    #else: stay
                else: # walk
                    if goal_B > B_foot:
                        B_foot += 1 # go
                    else : B_foot -= 1 # back

            if not robot: # 다음 로봇이 없고
                if not O:   # 오렌지 로봇 버튼이 끝나고
                    if not B: # 블루 로봇 버튼이 끝나고
                        if not goal_O: # 오렌지 로봇 목표가 끝나고
                            if not goal_B: # 블루 로봇 목표가 끝나면 정지
                                break;
        
        with open('output.txt', mode='a') as o_file:
            o_file.write('Case #')
            o_file.write(str(current))
            o_file.write(': ')
            o_file.write(str(turn))
            o_file.write('\n')
