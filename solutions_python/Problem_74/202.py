#! /usr/bin/python2

def main():
  # read in number of test cases
  ntc = int(raw_input())
  for i in range(ntc):
    words = raw_input().split(None)
    tasks_orange = []
    tasks_blue = []
    num_tasks = int(words[0])
    # prepare the tasks in a good order
    for task in range(num_tasks):
      robot = words[task*2+1]
      button = int(words[task*2+2])
      if robot == "O":
        tasks_orange.append(button)
      else:
        tasks_blue.append(button)
    # now prepare the data structures
    # where are the robots?
    pos_orange = 1
    pos_blue = 1
    # how many steps did they need?
    step_count = 0
    for task in range(num_tasks):
      robot = words[task*2+1]
      button = int(words[task*2+2])
      if robot == "O":
        # how far is the robot from the position?
        # that gives the steps he needs to be there and to press
        steps = abs(button - pos_orange) + 1
        # how far is the other robot from the position?
        # he will either go to his button or in that
        # direction
        if len(tasks_blue) > 0 and pos_blue > tasks_blue[0]:
          pos_blue -= min(steps, pos_blue - tasks_blue[0])
        elif len(tasks_blue) > 0 and pos_blue < tasks_blue[0]:
          pos_blue += min(steps, tasks_blue[0] - pos_blue)
        # take away the button the orange robot presses
        pos_orange = tasks_orange.pop(0)
      else:
        steps = abs(button - pos_blue) + 1
        if len(tasks_orange) > 0 and pos_orange > tasks_orange[0]:
          pos_orange -= min(steps, pos_orange - tasks_orange[0])
        elif len(tasks_orange) > 0 and pos_orange < tasks_orange[0]:
          pos_orange += min(steps, tasks_orange[0] - pos_orange)
        pos_blue = tasks_blue.pop(0)
      # add the steps to the problem
      step_count += steps
    # we are done and can output the result for the test case
    print "Case #{0}: {1}".format(i+1, step_count);

if __name__ == '__main__':
  main()
