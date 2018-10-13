#!/usr/bin/python

import sys

class Stats:
  def __init__(self):
    self.wp = 0.0
    self.owp = 0.0
    self.opponents = 0
    self.oowp = 0.0

# main function
# write code from here
def process(input, output):
  nb = int(input.readline().rstrip())
  for val in range(1, nb+1):
    # reading data
    inputs = input.readline().rstrip()

    teamCnt = int(inputs)

    stats = []
    results = []

    # Get results.
    for x in range(0, teamCnt):
      stats.append(Stats())
      r = []
      line = input.readline().rstrip()
      for y in range(0, teamCnt):
        r.append(line[y])
      results.append(r)

    # Get winning percentage.
    for x in range(0, teamCnt):
      for y in range(0, teamCnt):
        if results[x][y] == '1':
          stats[x].wp += 1.0
        if results[x][y] != '.':
          stats[x].opponents += 1

      stats[x].wp = stats[x].wp / stats[x].opponents

      for y in range(0, teamCnt):
        if x == y:
          continue
        opp = stats[x].opponents - 1
        if results[x][y] == '1':
          stats[y].owp += ((stats[x].wp * (opp + 1)) - 1) / opp
        elif results[x][y] == '0':
          stats[y].owp += stats[x].wp * (opp + 1) / opp

    # Make wp and owp flat.
    for x in range(0, teamCnt):
      stats[x].owp /= stats[x].opponents

    # Get oowp.
    for x in range(0, teamCnt):
      for y in range(0, teamCnt):
        if x == y or results[x][y] == '.':
          continue
        stats[x].oowp += stats[y].owp

      # Make it flat.
      stats[x].oowp /= stats[x].opponents

    output.write("Case #%d:\n" % val)
    for x in range(0, teamCnt):
      rpi = 0.25 * stats[x].wp + 0.50 * stats[x].owp + 0.25 * stats[x].oowp
      output.write('%s\n' % rpi)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Need file as argument"
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
