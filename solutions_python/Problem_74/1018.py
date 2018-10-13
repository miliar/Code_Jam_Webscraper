import sys
from collections import deque
from time import sleep

TARGET_ENDED = -1

qty_test_cases = int(sys.stdin.readline())

def find_new_target(robot):
    result = TARGET_ENDED
    
    for task in processing_queue:
        if task[0] == robot:
            result = task[1]
            break
    
    return result

for i in range(qty_test_cases):
    print "Case #%d:" % (i+1),
    
    robots_current_position = { "B": 1, "O": 1 }
    robots_target = { "B": None, "O": None }
    
    test_case = sys.stdin.readline().strip().split(" ")
    qty_movements = int(test_case[0])
    processing_queue = deque([(test_case[1:][x*2], int(test_case[1:][x*2+1])) for x in range(qty_movements)])
    
    time_slot = 0
    current_task = None
    
    while True:
        # -- refilling
        
        # find new targets if robot is idle
        for robot, target in robots_target.iteritems():
            if target is None:
                robots_target[robot] = find_new_target(robot)
        
        try:
            if current_task is None:
                current_task = processing_queue.popleft()
        except IndexError:
            break
        
        time_slot += 1
        
        # -- processing
        #print((robots_target[current_task[0]], robots_current_position[current_task[0]]))
        if robots_target[current_task[0]] == robots_current_position[current_task[0]]:
            robots_target[current_task[0]] = None
            #stat[current_task[0]] = "CLICK"
            current_task = None
        
        for robot, current, target in [(robot, current, robots_target[robot]) for robot, current in robots_current_position.iteritems()]:
            if not target is None and not target == TARGET_ENDED and not current == target:
                #stat[robot] = "1" if target > current else "-1"
                robots_current_position[robot] += 1 if target > current else -1
        
        #print stat, robots_target
    
    print time_slot