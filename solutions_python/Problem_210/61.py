def standardize(task):
  task.sort()
  last_person = task[-1][-1]
  i = 0
  while i < len(task) and task[i][-1] == last_person:
    i += 1

  if i == len(task):
    i = 0

  offset = task[i][0]

  for i in range(len(task)):
    task[i][0] -= offset
    task[i][1] -= offset

    if task[i][0] < 0:
      task[i][0] += 24*60
    if task[i][1] <= 0:
      task[i][1] += 24*60

  task.sort()

from collections import defaultdict

def duration(begin, end):
  d = end-begin
  if d >= 24*60:
    d -= 24*60
  if d < 0:
    d += 24*60
  return d

def process(task):
  interval = defaultdict(list)
  timespent = defaultdict(int)

  for i in range(len(task)):
    timespent[task[i][-1]] += duration(task[i][0], task[i][1])

    if task[i][-1] == task[i-1][-1]:
      interval[task[i][-1]].append(duration(task[i-1][1], task[i][0]))

  interval[0].sort()
  interval[1].sort()

  exchanges = len(task) + len(interval[0]) + len(interval[1])

  reduction = 0

  timeleft = 720 - timespent[0]
  for t in interval[0]:
    if t <= timeleft:
      reduction += 1
      timeleft -= t
    else:
      break

  timeleft = 720 - timespent[1]
  for t in interval[1]:
    if t <= timeleft:
      reduction += 1
      timeleft -= t
    else:
      break

  exchanges -= 2*reduction

  return exchanges



def run():
  T = int(raw_input().strip())

  for caseno in xrange(T):
    task = []

    AC, AJ = map(int, raw_input().strip().split())
    for i in range(AC):
      begin, end = map(int, raw_input().strip().split())
      task.append([begin, end, 0])

    for i in range(AJ):
      begin, end = map(int, raw_input().strip().split())
      task.append([begin, end, 1])

    standardize(task)

    answer = process(task)
    print "Case #" + str(caseno+1) + ": " + str(answer)

# task = [[0, 10, 0], [1420, 1440, 0], [90, 100, 0], [550, 600, 1], [900, 950, 1], [100, 150, 1], [1050, 1400, 1]]
# standardize(task)
# print process(task)

run()