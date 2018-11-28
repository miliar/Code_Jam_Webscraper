#!/usr/bin/env python

def main():
    T = int(raw_input())

    for i in range(T):
        task = raw_input().split()
        task = task[1:]

        (task_position, total_time, bonus_time, current_time) = (0, 0, 0, 0)
        positions = {"O": 1, "B": 1}
        current_robot = None

        while(task_position < len(task)):
        	current_robot = task[task_position]
        	to_position = int(task[task_position + 1])
        	task_position += 2

        	time_taken = abs(positions[current_robot] - to_position)
        	
        	if time_taken > bonus_time:
        		total_time += (time_taken - bonus_time)
        		current_time += (time_taken - bonus_time)
        	
        	current_time += 1
        	total_time += 1

        	positions[current_robot] = to_position
        	
        	if task_position < len(task) and task[task_position] is not current_robot:
        		bonus_time = current_time
        		current_time = 0
        	else:
        		bonus_time = 0

        print "Case #%d: %d" % (i+1, total_time)

if __name__ == "__main__":
    main()