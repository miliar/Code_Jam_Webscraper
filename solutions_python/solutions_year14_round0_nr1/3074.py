# codejam 2014 : qualifiers
# 1 : magic trick
import sys
from itertools import islice
from collections import namedtuple

Selection = namedtuple('Selection', ['first', 'second'])

def solve(first, second):
  common = first & second
  if not common:
    return 'Volunteer cheated!'
  elif len(common) > 1:
    return 'Bad magician!'
  else:
    return common.pop()

def parse_cards(input):
  answer = int(input.readline())
  cards = [input.readline() for _ in range(4)]
  return set(cards[answer-1].split())

def main(input):
  case_count = int (input.readline())
  for i in range(case_count):
    first = parse_cards(input)
    second = parse_cards(input)
    result = solve(first, second)
    print('Case #{0:n}: {1!s}'.format(i + 1, result))

if __name__ == '__main__':
  main(sys.stdin)