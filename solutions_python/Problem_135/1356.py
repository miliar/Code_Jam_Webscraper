def read_case():
  row1 = int(raw_input())
  arrangement1 = []
  for _ in range(4):
    row = map(int, raw_input().split())
    arrangement1.append(row)

  row2 = int(raw_input())
  arrangement2 = []
  for _ in range(4):
    row = map(int, raw_input().split())
    arrangement2.append(row)

  case_data = (row1, arrangement1, row2, arrangement2)
  return case_data


def solve_case(case_data):
  row1, arr1, row2, arr2 = case_data
  cards1 = arr1[row1-1]
  cards2 = arr2[row2-1]
  cards_intersection = intersection(cards1, cards2)
  n_intersection = len(cards_intersection)
  if n_intersection == 1:
    return cards_intersection[0]
  if n_intersection == 0:
    return "Volunteer cheated!"
  return "Bad magician!"


def intersection(a, b):
  return list(set(a) & set(b))


def read_and_solve():
  number_of_cases = int(raw_input())
  for case_number in range(1, number_of_cases + 1):
    data = read_case()
    answer = solve_case(data)
    print 'Case #%d: %s' % (case_number, answer)

if __name__ == '__main__':
  read_and_solve()
