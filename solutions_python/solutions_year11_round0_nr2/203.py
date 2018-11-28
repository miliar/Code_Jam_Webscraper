#!/usr/bin/env python

import collections

def ConvertInput(line, *conversion_functions):
  values = line.strip().split()
  return [f(v) for (f, v) in zip(conversion_functions, values)]
  

class Combinations:
  def __init__(self):
    self.graph = collections.defaultdict(lambda: (
      collections.defaultdict(lambda: False)))

  def AddCombination(self, a, b, combination):
    self.graph[a][b] = combination
    self.graph[b][a] = combination

  def IsCombination(self, a, b):
    return self.graph[a][b] != False

  def GetCombinationResult(self, a, b):
    return self.graph[a][b]


class Oppositions:
  def __init__(self):
    self.graph = collections.defaultdict(lambda: list())
    return
  
  def AddOpposition(self, a, b):
    self.graph[a].append(b)
    self.graph[b].append(a)
    return

  def GetOppositionElements(self, a):
    return self.graph[a]



class MagickaBoard:
  def __init__(self):
    self.oppositions = Oppositions()
    self.combinations = Combinations()

    self.letters = collections.defaultdict(lambda: 0)
    self.board = []

  def AddOpposition(self, a, b):
    self.oppositions.AddOpposition(a, b)
    return

  def AddCombination(self, a, b, c):
    self.combinations.AddCombination(a, b, c)
    return

  def AddElement(self, element):
    # Handle empty board
    if self.board == []:
      self.board = [element]
      assert all([self.letters[i] == 0 for i in self.letters.keys()])
      self.letters[element] += 1
      return

    top_element = self.board[-1]
    if self.combinations.IsCombination(top_element, element):
      new_element = self.combinations.GetCombinationResult(top_element, element)
      self.letters[top_element] -= 1
      self.letters[new_element] += 1
      self.board[-1] = new_element
      return

    # Check oppositions
    for e in self.oppositions.GetOppositionElements(element):
      if self.letters[e] > 0:
        self.board = []
        self.letters = collections.defaultdict(lambda: 0)
        return
   
    self.board.append(element)
    self.letters[element] += 1
    return


def ProcessTestCase(test_case):
  m = MagickaBoard()

  elements = raw_input().strip().split()
  c = int(elements[0])

  for s in elements[1:c+1]:
    m.AddCombination(s[0], s[1], s[2])

  # Shift away everything till D
  elements = elements[c+1:]
  c = int(elements[0])
  for s in elements[1:c+1]:
    m.AddOpposition(s[0], s[1])

  # Shift away everything till N
  elements = elements[c+1:]
  for char in elements[1]:
    m.AddElement(char)
  print "Case #%d: %s"%(test_case+1, ListToStr(m.board))
  # print "Oppositions: %s"%(m.oppositions.graph)
  return

def ListToStr(li):
  return "[" + ", ".join([str(x) for x in li]) + "]"


def Main():
  test_cases = ConvertInput(raw_input(), int)[0]
  for t in range(test_cases):
    ProcessTestCase(t)


if __name__ == '__main__':
  Main()
