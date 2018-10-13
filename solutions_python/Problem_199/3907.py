input_name = "example" 
input_name = "A-small-attempt0" 
# input_name = "A-largea" 
inputs = list()
flips = list()
pancakes = list()
solutions = list()

# funcs
def convertPancakes(pnk):
  return pnk.replace('-', '0').replace('+', '1')
def inversePancakes(pnk):
  return convertPancakes(pnk.replace('0', '+').replace('1', '-'))
def flipPancakes(pancakes, nums):
  res = list()
  for pnk in pancakes:
    for x in range(0, len(pnk) - nums + 1):
      # print '\n>>>>'
      # print pnk[0:x], pnk[x:x+nums], pnk[x+nums:len(pnk)], pnk[0:x] + pnk[x:x+nums] + pnk[x+nums:len(pnk)]
      # print "inv", pnk[0:x] + inversePancakes(pnk[x:x+nums]) + pnk[x+nums:len(pnk)]
      res.append(pnk[0:x] + inversePancakes(pnk[x:x+nums]) + pnk[x+nums:len(pnk)])
  return res

# input
fi = open(input_name + '.in', 'r')
for line in fi:
  inputs.append(line.strip())

cases = inputs[1:]
for case in cases:
  inp = case.split(' ')
  pancakes.append(convertPancakes(inp[0]))
  flips.append(int(inp[1]))
print 'Flips: ', flips
print 'pancakes: ', pancakes

# solution
prevList = list()
for x in range(0, len(pancakes)):
  if (pancakes[x].count('0') == 0):
    print ":: CASE (pn, flips) ::", pancakes[x], flips[x]
    solutions.append(0)
    continue
  else: 
    print ":: CASE (pn, flips) ::", pancakes[x], flips[x]
    flipped = [pancakes[x]]
    # print flipped
    sol = '1' * len(pancakes[x])
    for z in range(0, 1000):
      flipped = flipPancakes(flipped, flips[x])
      flipped = list(set(flipped))
      if (sol in flipped):
        solutions.append(z + 1)
        break
      if (len(prevList) == len(flipped)):
        solutions.append(-1)
        prevList = list()
        break
      # print prevList, flipped
      prevList = flipped

print 'Solutions: ', solutions

# output
fo = open(input_name + '.out', 'w')
for x in range(0, len(solutions)):
  fo.write(('Case #' + str(x + 1) + ': ' + str(solutions[x]) + '\n').replace(': -1', ': IMPOSSIBLE'))

# closure
fi.close()
fo.close()