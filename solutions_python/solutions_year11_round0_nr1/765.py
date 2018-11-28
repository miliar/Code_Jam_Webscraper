import sys

def max(a, b):
  if (a > b):
    return a
  else:
    return b

def get_other_robot(active_robot):
  if (active_robot == "O"):
    return "B"
  else:
    return "O"

def process_line(line):
  N = line[0]
  items = line[1:]
  
  last_action_finish_time = {}
  last_action_finish_time["O"] = 0
  last_action_finish_time["B"] = 0

  positions = {}
  positions["O"] = 1
  positions["B"] = 1
  
  while (items):
    active_robot = items[0]
    other_robot = get_other_robot(active_robot)
    robot_target = int(items[1])
    items = items[2:]
    
    move_length = abs(robot_target - positions[active_robot])
    button_arrival_time = last_action_finish_time[active_robot] + move_length
    button_press_time = max(button_arrival_time, last_action_finish_time[other_robot])
    last_action_finish_time[active_robot] = button_press_time + 1
    positions[active_robot] = robot_target
    
  return max(last_action_finish_time["O"], last_action_finish_time["B"])
    
  

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  line = [v for v in infile.readline().split()]
  
  print process_line(line)
  
infile.close()