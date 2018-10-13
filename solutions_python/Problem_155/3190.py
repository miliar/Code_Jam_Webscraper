import os
import sys
import os.path
import logging

logging.basicConfig(level = logging.DEBUG,
                    datefmt = '%m-%d %H:%M',
                    format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    filename = 'debug.log',
                    filemode = "w")

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)

inputLog = logging.getLogger("input") 
algoLog = logging.getLogger("algo")

with open(sys.argv[1], "r") as f:
  num_cases = int(f.readline())
  inputLog.debug("num_cases = %s", num_cases)

  for case in range(1,num_cases+1):
    line = f.readline().split(' ')
    s_max = int(line[0])
    persons = line[1]

    inputLog.debug("case #%d: s_max=%d, persons=%s", case, s_max, persons.strip())
    total = int(persons[0])
    missing = 0

    for i in range (1,s_max+1):
      if total < i:
        missing += i - total
        algoLog.debug("case #%d: s=%d, missing %d persons, total persons=%d, total_missing=%d", case, i, i-total, total, missing)
        total = i
      else:
        algoLog.debug("case #%d: s=%d, total=%d", case, i, total)

      total += int(persons[i])
      if total > s_max:
        break

    print("Case #{}: {}".format(case, missing))

