MAGICIAN_ERROR = 'Bad magician!'
VOLUNTEER_ERROR = 'Volunteer cheated!'

def main():
  cases_count = int(raw_input())
  for i in xrange(cases_count):
    rows = []
    for turn_index in xrange(2):
      answer = int(raw_input()) - 1
      for j in xrange(answer):
        raw_input()
      rows.append({int(card) for card in raw_input().split()})
      for j in xrange(3 - answer):
        raw_input()
    print 'Case #{}: {}'.format(i + 1, solve_trick(rows))

def solve_trick(rows):
  cards = rows[0] & rows[1]
  if not cards:
    return VOLUNTEER_ERROR
  elif len(cards) == 1:
    return next(iter(cards))
  else:
    return MAGICIAN_ERROR
    
if __name__ == '__main__':
  main()