#!/usr/bin/python3
import sys

def recurring(numbers):
  result = []
  for n in numbers:
    if numbers.count(n) > 1 and (n not in result):
      result.append(n)

  return result

def answer(case, first, fcards, second, scards):
  cards = fcards[first] + scards[second]
  cards = recurring(cards)
  if len(cards) == 1:
    print ("Case #{}: {}".format(case, cards[0])) 
  elif len(cards) == 0:
    print ("Case #{}: Volunteer cheated!".format(case)) 
  else:
    print ("Case #{}: Bad magician!".format(case)) 
  
def line():
  return sys.stdin.readline().strip()

def read_case():
  case = []
  for i in range(2):
    row = int(line()) - 1 
    cards = []
    for i in range(4):
      cards.append(line().split(" "))
    case.append(row)
    case.append(cards)
  
  return case

cases = int(line())
for i in range(cases):
  answer(i + 1, *read_case())
