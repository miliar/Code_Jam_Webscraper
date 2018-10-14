#!/usr/bin/python

def readfile(file):
  """
    input:

    T (number of test cases)
    N ([OB] n)+

    N - number of buttons required
    O n - Orange bot has to hit button n
    B n - Blue bot has to hit button n
  """

  tests = []

  T = int(file.readline().strip())

  for i in xrange(T):
    test = []
    
    line = file.readline().strip()

    parts = line.split(" ")
    index = 0

    N = int(parts[index])
    index = index + 1

    for j in xrange(N):
      bot = parts[index]
      index = index + 1

      button = int(parts[index])
      index = index + 1

      task = (bot, button)

      test.append(task)

    tests.append(test)

  return tests

def sign(x):
  if x < 0:
    return -1
  elif x > 0:
    return 1
  else:
    return 0

def calculateTask(myTasks, myCurTask, theirTasks):
  """
    Processes one task

    Returns (time taken -1 on blocked/finished, finishes task)

    Task is (curPosition, desiredPosition, pushButton, blockingTask, finished).
  """

  canDo = False

  if (myCurTask < len(myTasks)):
    # Have things to do
    if ((myTasks[myCurTask][3] >= 0) and (myTasks[myCurTask][0] == myTasks[myCurTask][1])):
      # Blocked
      canDo = False

      # Is the corresponding task done?
      blockingTask = myTasks[myCurTask][3]
      if (theirTasks[blockingTask][4]):
        # Finished
        canDo = True

    else:
      # Stuff to do
      canDo = True

  if canDo:
    if (myTasks[myCurTask][0] != myTasks[myCurTask][1]):
      # Need to move
      return (abs(myTasks[myCurTask][1] - myTasks[myCurTask][0]), not myTasks[myCurTask][2])
    elif (myTasks[myCurTask][2]):
      return (1, True)
    else:
      return (0, True)
  else:
    return (-1, False)

def executeTask(taskCost, myTasks, curTask):
  """
    Returns (time taken, new cur task)

    Task is (curPosition, desiredPosition, pushButton, blockingTask, finished).
  """

  if taskCost[1]:
    # Must be finished
    myTasks[curTask][4] = True
    return (taskCost[0], curTask + 1)
  else:
    # Moving, still need to button
    direction = sign(myTasks[curTask][1] - myTasks[curTask][0])
    myTasks[curTask][0] = myTasks[curTask][0] + direction * taskCost[0]
    return (taskCost[0], curTask)

def processTask(orangeTasks, curOrangeTask, blueTasks, curBlueTask):
  """
    Processes one set of stuff.

    Returns (time taken, curOrangeTask, curBlueTAsk)

    Task is (curPosition, desiredPosition, pushButton, blockingTask, finished).
  """

  # Get costs of executing each task
  orangeCost = calculateTask(orangeTasks, curOrangeTask, blueTasks)
  blueCost = calculateTask(blueTasks, curBlueTask, orangeTasks)

  # See who has stuff to do
  if ((orangeCost[0] < 0) and (blueCost[0] < 0)):
    # Done maybe?
    return -1
  elif (orangeCost[0] < 0):
    # Only blue has things to do
    result = executeTask(blueCost, blueTasks, curBlueTask)

    return (result[0], curOrangeTask, result[1])
  elif (blueCost[0] < 0):
    # Only orange has things to do
    result = executeTask(orangeCost, orangeTasks, curOrangeTask)

    return (result[0], result[1], curBlueTask)
  else:
    # Both have things to do, figure out who gets what
    oc = 0
    bc = 0

    if (orangeCost[1] and blueCost[1]):
      # Both finished
      orangeTasks[curOrangeTask][4] = True
      blueTasks[curBlueTask][4] = True

      return (1, curOrangeTask + 1, curBlueTask + 1)
    elif not (orangeCost[1] or blueCost[1]):
      # None finished
      # Move the minimum
      move = min(orangeCost[0], blueCost[0])

      direction = sign(orangeTasks[curOrangeTask][1] - orangeTasks[curOrangeTask][0])
      orangeTasks[curOrangeTask][0] = orangeTasks[curOrangeTask][0] + direction * move

      direction = sign(blueTasks[curBlueTask][1] - blueTasks[curBlueTask][0])
      blueTasks[curBlueTask][0] = blueTasks[curBlueTask][0] + direction * move

      return (move, curOrangeTask, curBlueTask)

    else:
      # One of the two finished
      if (orangeCost[1]):
        # Button push, do it
        oc = 1
        orangeTasks[curOrangeTask][4] = True
        curOrangeTask = curOrangeTask + 1
      elif (orangeCost[0] > 0):
        # Move one square
        oc = 1
        direction = sign(orangeTasks[curOrangeTask][1] - orangeTasks[curOrangeTask][0])
        orangeTasks[curOrangeTask][0] = orangeTasks[curOrangeTask][0] + direction * 1

      if (blueCost[1]):
        # Button push do it
        bc = 1
        blueTasks[curBlueTask][4] = True
        curBlueTask = curBlueTask + 1
      elif (blueCost[0] > 0):
        # Move one square
        bc = 1
        direction = sign(blueTasks[curBlueTask][1] - blueTasks[curBlueTask][0])
        blueTasks[curBlueTask][0] = blueTasks[curBlueTask][0] + direction * 1

      return (max(oc, bc), curOrangeTask, curBlueTask)


def run(test):
  """
    Task is (curPosition, desiredPosition, pushButton, blockingTask, finished).
  """

  result = 0

  # Build task lists
  orangeTasks = []
  blueTasks = []

  curOrangeTask = 0
  curBlueTask = 0

  co = -1
  cb = -1

  po = 1
  pb = 1

  for task in test:
    if (task[0] == 'O'):
      orangeTasks.append([po, task[1], True, cb, False])
      po = task[1]
      co = co + 1
    elif (task[0] == 'B'):
      blueTasks.append([pb, task[1], True, co, False])
      pb = task[1]
      cb = cb + 1

  #print test
  #print "orange: %s" % (orangeTasks)
  #print "blue: %s" % (blueTasks)

  while (curOrangeTask < len(orangeTasks)) or (curBlueTask < len(blueTasks)):
    # Figure out what happens
    (cost, curOrange, curBlue) = processTask(orangeTasks, curOrangeTask, blueTasks, curBlueTask)

    #print "(%d, %d, %d)" % (cost, curOrange, curBlue)
    #print "orange: %s" % (orangeTasks)
    #print "blue: %s" % (blueTasks)

    if (cost < 0):
      print "Something went horribly wrong"
      break
    else:
      result = result + cost
      curOrangeTask = curOrange
      curBlueTask = curBlue

  return result 

file = open("A-large.in.txt", "rt")

tests = readfile(file)

case = 1

for test in tests:
#if True:
  #test = tests[0]
  result = run(test)
  print "Case #%d: %s" % (case, result)
  case = case + 1

file.close()
