import sys

tests = sys.stdin.readline()

output = ""

for i in range(0, int(tests)):
  
  line = sys.stdin.readline().split()
  chars = list(line[1])
  ppl = 0
  added = 0

  # print "Case #" + str(i)

  for p in range(0, len(chars)):
    curr = int(chars[p])
    # print "p:", p, "curr:", curr, "ppl:", ppl
    
    if (curr > 0 and ppl < p):
      # print "ADDING PEOPLE"
      to_add = p - ppl
      added += to_add
      ppl += to_add
    
    ppl += curr

  # print "Added:", added, "people"
  output += "Case #" + str(i + 1) + ": " + \
            str(added) + "\n"

print output