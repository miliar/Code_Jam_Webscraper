def run():
  test_case_count = int(raw_input())  # read a line with a single integer
  for i in range(1, test_case_count + 1):
    biggest_candidate = [int(x) for x in raw_input()]

    print("Case #{}: {}".format(i, "".join(map(str, last_tidy(biggest_candidate)))))

def last_tidy(biggest_candidate):
  # pseudocode:
  # go to the right keeping track of equalities
  # go to the right until you find an issue eee Lll l > R rrr
  # replace lll R rrr with that many 9s
  # replace L with L - 1 (or if 1, replace it with nothing)

  equality_start_idx = 0

  for idx in range(len(biggest_candidate) - 1):
    cur, nxt = biggest_candidate[idx], biggest_candidate[idx+1]

    if cur < nxt:
      # so much for equality
      equality_start_idx = idx + 1
    elif cur > nxt: # found the tidy break
      # turn everything to the left of equality start into 9s
      end_piece = [9] * (len(biggest_candidate) - equality_start_idx - 1)
      # keep right piece as it is
      start_piece = biggest_candidate[0:equality_start_idx]
      # mid piece is either n-1 or goes away in case of 1
      mid_piece = [cur - 1] if cur > 1 else []
      return start_piece + mid_piece + end_piece

  # I guess it was tidy this entire time
  return biggest_candidate

run()
