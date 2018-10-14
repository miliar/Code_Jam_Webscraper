def line_to_int(line):
  return int(line.rstrip())

def solve_case(fp, case_nb):
  C, F, X = [ float(i) for i in fp.readline().rstrip().split(" ") ]

  R = 2.0 # current rate of producing cookies

  time_so_far = 0

  while True:
    # compute first time to X with buying a C
    time_with_c = C / R + X / (R+F)
    time_without_c = X / R

    if time_with_c > time_without_c:
      print "Case #%s: %.6f" % (case_nb+1, time_so_far + time_without_c)
      break
    else:
      time_so_far += C / R
      R = R + F

def solve():
  with open("B-large.in", "r") as fp:
    T = line_to_int(fp.readline())

    for i in range(T):
      solve_case(fp, i)

if __name__ == "__main__":
  solve()
