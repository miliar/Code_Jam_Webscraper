#!/usr/bin/python

from sys import stdin

def play_magicka(combine, opposed, play):
  # Pre-process combine
  combine_dict = {}

  for a, b, r in combine:
    combine_dict[a + b] = r
    combine_dict[b + a] = r

  # Process opposed
  opposed_dict = {}
  
  for a, b in opposed:
    opposed_dict.setdefault(a, set())
    opposed_dict[a].add(b)
    opposed_dict.setdefault(b, set())
    opposed_dict[b].add(a)

  # Play the game
  play = list(play)
  play.reverse()
  element = play.pop()
  elements = []
  element_types = dict()
  
  while True:
    if elements:
      combined = combine_dict.get(elements[-1] + element, None)
      if combined:
        e = elements.pop()
        element_types[e] -= 1
        element = combined
        continue

      opposed = opposed_dict.get(element, ())

      for e in opposed:
        if e == element or element_types.get(e, 0):
          elements = []
          element_types = dict()

          if not play:
            return elements
          element = play.pop()
          continue

    elements.append(element)
    element_types[element] = element_types.get(element, 0) + 1

    if not play:
      return elements

    element = play.pop()
    

def evaluate_case(case):
  opcodes = case.strip().split(' ')

  c = int(opcodes[0]) + 1
  combine = opcodes[1:c]

  d = c + int(opcodes[c]) + 1
  opposed = opcodes[c+1:d]

  elements = opcodes[d+1]

  elements = play_magicka(combine, opposed, elements)
  return '[' + ', '.join(elements) + ']'
    
cases = stdin.readlines()
count = int(cases[0])

for i in range(1, count+1):
  print('Case #' + str(i) + ': ' + evaluate_case(cases[i]))
