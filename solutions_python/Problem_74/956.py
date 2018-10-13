import math

f = open('input.txt', 'r')
output = ""

n = int(f.readline())
for i in range(0, n):
  O = 1
  B = 1
  nextO = nextB = 0
  tasks = []
  
  cs = f.readline().split(' ');
  for j in range(1, len(cs), 2):
    if cs[j] == 'O':
      if nextO == 0:
        nextO = int(cs[j + 1])
      tasks.append({'hall': 'O', 'btn': int(cs[j + 1])})
    elif cs[j] == 'B':
      if nextB == 0:
        nextB = int(cs[j + 1])
      tasks.append({'hall': 'B', 'btn': int(cs[j + 1])})
  
  completed = 0
  seconds = 0
  while completed < len(tasks):
    if tasks[completed]['hall'] == 'O':
      # The action of O
      if O == tasks[completed]['btn']:
        completed = completed + 1
        for k in range(completed + 1, len(tasks)):
          if tasks[k]['hall'] == 'O':
            nextO = tasks[k]['btn']
            break
      else:
        O = O + math.copysign(1, tasks[completed]['btn'] - O)
        
      # The action of B
      if nextB != B:
        B = B + math.copysign(1, nextB - B)
    else:
      # The action of B
      if B == tasks[completed]['btn']:
        completed = completed + 1
        for k in range(completed + 1, len(tasks)):
          if tasks[k]['hall'] == 'B':
            nextB = tasks[k]['btn']
            break
      else:
        B = B + math.copysign(1, tasks[completed]['btn'] - B)
        
      # The action of O
      if nextO != O:
        O = O + math.copysign(1, nextO - O)
  
    seconds = seconds + 1
  
  output = output + "Case #%d: %d" % (i + 1, seconds)
  output = output + "\n"
  
f = open('output.txt', 'w')
f.write(output)
