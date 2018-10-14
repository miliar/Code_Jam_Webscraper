from itertools import product
import fileinput

def parse(challenge):
  '''
  The first line of the input gives the number of test cases, T. T
  test cases follow. Each test case starts with a line containing an
  integer: the answer to the first question. The next 4 lines
  represent the first arrangement of the cards: each contains 4
  integers, separated by a single space. The next line contains the
  answer to the second question, and the following four lines contain
  the second arrangement in the same format.
  '''
  cases = int(challenge[0])
  assert(len(challenge) == cases * 10 + 1)
  data = []
  for i in range(cases):
    c = lambda l: int(l)
    m = lambda l: map(lambda e: map(int, e.split()), l)
    choice1 = c(challenge[i*10+1:i*10+6][0])
    matrix1 = m(challenge[i*10+1:i*10+6][1:])
    choice2 = c(challenge[i*10+6:i*10+11][0])
    matrix2 = m(challenge[i*10+6:i*10+11][1:])
    data += [
        ((matrix1, matrix2),
        (choice1, choice2),)
        ]
  return data


def guess(arrangements, choices):
    assert(len(arrangements) == 2)
    assert(len(choices) == 2)

    matches = filter(
        lambda p: p[0] == p[1],
        product(
          arrangements[0][choices[0]-1], 
          arrangements[1][choices[1]-1]
          )
        )

    n_matches = len(matches)
    if n_matches > 1:
      return 'Bad magician!'
    elif n_matches == 1:
      return matches[0][0]
    elif n_matches == 0:
      return 'Volunteer cheated!'
    else:
      raise Exception()

T = parse([line for line in fileinput.input()])
for index, (arrangement, choice) in enumerate(T):
  print 'Case #%d: %s' % (index+1, guess(arrangement, choice))
