
if __name__ == '__main__':
  num_test_cases = int(raw_input())
  for tc in range(1, num_test_cases+1):
    first_answer = int(raw_input())
    first_selected = set()
    for row in range(1,5):
      row_of_numbers = map(int, raw_input().split())
      if row == first_answer:
        first_selected.update(row_of_numbers)
    second_answer = int(raw_input())
    second_selected = set()
    for row in range(1,5):
      row_of_numbers = map(int, raw_input().split())
      if row == second_answer:
        second_selected.update(row_of_numbers)

    common = first_selected.intersection(second_selected)

    if len(common) == 1:
      print 'Case #%d: %d' % (tc, common.pop())
    elif len(common) > 1:
      print "Case #%d: Bad magician!" % tc
    elif len(common) == 0:
      print "Case #%d: Volunteer cheated!" % tc

