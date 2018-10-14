def line_to_int(line):
  return int(line.rstrip())

def read_matrix(fp):
  lines = []
  for i in range(4):
    lines.append([ int(nb) for nb in fp.readline().rstrip().split(" ") ])

  return lines

def solve_case(fp, case_nb):
  first_row = line_to_int(fp.readline())
  matrix = read_matrix(fp)

  first_set = set(matrix[first_row-1])

  second_row = line_to_int(fp.readline())
  matrix = read_matrix(fp)

  second_set = set(matrix[second_row-1])

  intersection = first_set & second_set

  if len(intersection) == 1:
    print "Case #%s: %s" % (case_nb+1, intersection.pop())
    return 

  if len(intersection) > 1:
    print "Case #%s: %s" % (case_nb+1, "Bad magician!")
  if len(intersection) == 0:
    print "Case #%s: %s" % (case_nb+1, "Volunteer cheated!")

def solve():
  with open("A-small-attempt0.in", "r") as fp:
    T = line_to_int(fp.readline())

    for i in range(T):
      solve_case(fp, i)

if __name__ == "__main__":
  solve()
