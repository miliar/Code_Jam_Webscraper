from string import split
from math import copysign

def parse(filename):
  f = open(filename, 'r')
  t = int(f.readline()[:-1])
  data = []
  for iline in range(t):
    line = split(f.readline()[:-1])
    n = int(line.pop(0))
    orders = {'O':[], 'B':[]}
    for norder in range(n, 0, -1):
      pos   = int(line.pop())
      robot = line.pop()
      orders[robot].append((norder, pos))
    data.append(orders)
  f.close()
  return data

def main(fileprefix):
  data = parse(fileprefix + '.in')
  f = open(fileprefix + '.out', 'w')
  i = 1;
  for trial in data:
    export('Case #{0:d}: {1:d}'.format(i, calc(trial)), f)
    i += 1;
  f.close()

def export(str, file):
  print str
  file.write(str + '\n')

def calc(data):
  time = 0
  pos = {'O':1,'B':1}
  while data['O'] or data['B']:
      time += advancetime(data, pos)
  return time

def advancetime(data, pos):
  if not data['O']:
    b = data['B'].pop()[1]
    time = abs(b - pos['B']) + 1
    o = pos['O']
  elif not data['B']:
    o = data['O'].pop()[1]
    time = abs(o - pos['O']) + 1
    b = pos['B']
  elif data['B'][-1][0] < data['O'][-1][0]:
    b = data['B'].pop()[1]
    time = abs(b - pos['B']) + 1
    o = move(pos['O'], data['O'][-1][1], time)
  else:
    o = data['O'].pop()[1]
    time = abs(o - pos['O']) + 1
    b = move(pos['B'], data['B'][-1][1], time)
  #print 'b moves from {0:d} to {1:d}'.format(pos['B'], b)
  #print 'o moves from {0:d} to {1:d}'.format(pos['O'], o)
  #print 'in {0:d} seconds\n'.format(time)
  pos['O'], pos['B'] = o, b
  return time

def move(pos, goal, time):
  if abs(pos - goal) <= time:
    return goal
  else:
    return pos + int(copysign(time, goal - pos))

