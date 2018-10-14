
f = open("C-small-attempt0.in", "r")

cases = []
for line in f:
  cases.append(line)

length = int(cases.pop(0))

results = {}
for i in range(len(cases)):
  print cases[i][1]
  cases[i] = cases[i].split()
  for j in range(len(cases[i])):
    cases[i][j] = int(cases[i][j])
  if cases[i][0] < 10 and cases[i][1] < 10:
    results[i] = 0

print cases
print results

def check_recycled(num1, num2):
  #12, 21, 13, 31, 23, 32
  #return null
  pairs = []
  a = num1
  b = a+1

  while a < b and a < num2:
    while b < (num2+1):
      if (len(str(a))) == (len(str(b))):
        for i in range(len(str(a))):
	  part1 = str(a)[i:]
	  part2 = str(a)[:i]
	  if b == int(part1 + part2):
	    pairs.append(str(b) + str(int(part2 + part1)))
      b += 1
    a += 1
    b = a+1
  
  return len(list(set(pairs)))

for i in range(len(cases)):
  results[i] = check_recycled(cases[i][0], cases[i][1])

output = []
for key in results:
  output.append("Case #" + str(key+1) + ": " + str(results[key]) + "\n")

print output
w = open("output.out", "w")
w.writelines(output)
w.close()


print results

