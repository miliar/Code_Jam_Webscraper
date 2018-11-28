print "Hello world!"

def solve(line):
  elements = line.split()
  combines = {}
  c = int(elements[0])
  for i in range(1, c + 1):
    item = elements[i]
    combines[(item[0], item[1])] = item[2]
    combines[(item[1], item[0])] = item[2]
  d = int(elements[c + 1])
  clears = {}
  for j in range((c + 1) + 1, (c + 1) + d + 1):
    item = elements[j]
    clears[item[0]] = clears.get(item[0],"") + item[1]
    clears[item[1]] = clears.get(item[1],"") + item[0]
  # print combines
  # print clears

  letters = elements[(c + 1) + (d + 1) + 1]
  result = []
  for letter in letters:
    result.append(letter)
    # does it combine?
    last = result[-2:]
    if len(last) == 2:
      combined = combines.get((last[0], last[1]), None)
      if combined:
         result = result[:-2] + [combined]
      # Does this letter clear?
      else:
        for aletter in result[:-1]:
          if aletter in clears.get(letter, ""):
             result = []
             continue
             # print "Cleared();"
       
  return "[%s]" % (", ".join(result))

f = open("b-large.in", "r")
f2 = open("b-large.out", "w")
lines = f.readlines()
f.close()


cases = int(lines[0])
for case in range(0, cases):
  f2.write ("Case #%d: %s\n" % (case + 1, solve(lines[case + 1])))

f2.close()
