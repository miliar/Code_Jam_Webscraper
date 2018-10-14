def read_case():
  _ = int(raw_input())
  row1 = map(float, raw_input().split())
  row2 = map(float, raw_input().split())
  return row1, row2


def solve_case(player1, player2):
  # player's blocks masses in kg
  points_war = solve_war(player1, set(player2))
  points_deceive = solve_deceive(player1, set(player2))
  return '%s %s' % (points_deceive, points_war)


def solve_war(player1, player2):
  # optimal strategy
  points = 0
  for chosen_p1 in player1:
    bigger = filter(lambda x: x > chosen_p1, player2)
    if bigger:
      chosen_p2 = sorted(bigger)[0]
      player2.remove(chosen_p2)
    else:
      player2.remove(sorted(player2)[0])
      points += 1
  return points


def solve_deceive(player1, player2):
  points = 0
  l1 = list(sorted(player1))
  l2 = list(sorted(player2))
  points = 0
  while(len(l1)):
    if l1[0] > l2[0]:
      # tell the biggest, player2 give the lowest
      del l1[0]
      del l2[0]
      points += 1
    else:
      del l1[0]
      del l2[-1]
  return points


def read_and_solve():
  number_of_cases = int(raw_input())
  for case_number in range(1, number_of_cases + 1):
    data = read_case()
    answer = solve_case(*data)
    print 'Case #%d: %s' % (case_number, answer)

if __name__ == '__main__':
  read_and_solve()
