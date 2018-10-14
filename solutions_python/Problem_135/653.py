
def solve(fname):
  output = open("output.txt", "w+")
  with open(fname, "r") as f:
    numCases = int(f.readline())

    for i in xrange(numCases):
      firstAnswer = int(f.readline()) - 1

      firstArrangement = [ ]
      for j in xrange(4):
        row = f.readline().strip().split(" ")
        row = [int(element) for element in row]

        firstArrangement.append(row)

############################################################################

      secondAnswer = int(f.readline()) - 1

      secondArrangement = [ ]
      for j in xrange(4):
        row = f.readline().strip().split(" ")
        row = [int(element) for element in row]

        secondArrangement.append(row)

      firstRow = set(firstArrangement[firstAnswer])
      secondRow = set(secondArrangement[secondAnswer])
      solution = firstRow.intersection(secondRow)

      line = "Case #{}: {}\n"

      if len(solution) is 0:
        output.write(line.format(i+1, "Volunteer cheated!"))
      elif len(solution) is 1:
        output.write(line.format(i+1, list(solution)[0]))
      else:
        output.write(line.format(i+1, "Bad magician!"))


solve("input.in")

