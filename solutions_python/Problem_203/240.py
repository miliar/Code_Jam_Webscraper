from copy import deepcopy

def run():
  test_case_count = int(raw_input())  # read a line with a single integer
  for case in range(1, test_case_count + 1):

    case_lines = []
    size_line = raw_input()
    row_count, col_count = [int(x.strip()) for x in size_line.split(" ")]
    for row in range(row_count):
      case_lines.append(list(raw_input()))

    solution = solve_cake(case_lines)
    print("Case #{}:".format(case))
    #for line in case_lines:
    #  print("".join(line))
    for line in solution:
      print("".join(line))

def solve_cake(case_lines):
  answer = deepcopy(case_lines)

  row_fill_me_later = []
  fill_me_later = []
  for idx_r, row in enumerate(case_lines):
    current_cell = None
    # if row is trivially empty, just fill from above

    if all(x == "?" for x in row):
      if idx_r == 0 or idx_r - 1 in row_fill_me_later:
        row_fill_me_later.append(idx_r)
      else:
        answer[idx_r] = answer[idx_r-1]
    else:
      for idx_c, cell in enumerate(row):
        if cell == "?":
          if current_cell:
            answer[idx_r][idx_c] = current_cell
          else:
            fill_me_later.append((idx_r, idx_c))
        else:
          # print "I found " + cell
          # real value
          current_cell = cell
          above_cell = answer[idx_r-1][idx_c]
          fill_from_above = (idx_r > 0 and idx_c > 0 and
               above_cell != answer[idx_r-1][idx_c-1])
          # decide if to fill previous from down or this guy
          # fill from above IFF above

          for r, c in fill_me_later:
            #print "filling {}" "from_above? {}".format((r, c), fill_from_above)
            #print "above_cell was {}".format(above_cell)
            answer[r][c] = answer[r-1][c] if fill_from_above else current_cell
          fill_me_later = []

      # fill empty rows
      for up_row_idx in row_fill_me_later:
        answer[up_row_idx] = answer[idx_r]
      row_fill_me_later = []


  return answer
run()
