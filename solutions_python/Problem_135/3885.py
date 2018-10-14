import sys

def solve(numberOfCases, it):
  for caseNumber in range(1, int(numberOfCases)+1):
    first_candidates = get_numbers_in_row(it, int(it.next()))
    second_candidates = get_numbers_in_row(it, int(it.next()))

    solutions = getCommonNumbers(first_candidates, second_candidates)

    prefix = 'Case #' + str(caseNumber) + ': '
    if len(solutions) > 1:
      print prefix + 'Bad magician!'
    elif len(solutions) is 0:
      print prefix + 'Volunteer cheated!'
    else:
      print prefix + solutions[0]

def get_numbers_in_row(it, guessedRow):
  for rowNum in range(1, 5):
    if rowNum == guessedRow:
      line = it.next()
    else:
      it.next()
  return line.split()

def getCommonNumbers(firstArray, secondArray):
  return list(set(firstArray).intersection(secondArray))

it = sys.stdin.xreadlines()
solve(it.next(), it)