#!/usr/bin/python

M = 4

def intersect(a, b):
  return list(set(a) & set(b))


def readfile(filepath):
  with open(filepath, 'r') as f:
    for line in f:
      yield line.rstrip()


lines = readfile('smallInput.txt')
cases = None
choice = None
cards = []
picks = []
current_case = 1

for line in lines:
  if cases is None:
    cases = int(line)
    continue
  if choice is None:
    choice = int(line)
    continue

  if len(cards) < M:
    cards.append(line)
    if len(cards) == M:
        picks.append(cards[choice-1].split(' '))
        choice = None
        cards = []
    if len(picks) < 2:
      continue
    else:
      card = intersect(picks[0],picks[1])
      if len(card) == 1:
        print 'Case #%d: %d' % (current_case,int(card[0]))
      elif len(card) == 0:
        print 'Case #%d: Volunteer cheated!' % (current_case)
      else:
        print 'Case #%d: Bad magician!' % (current_case)
      picks = []
      current_case += 1
  
