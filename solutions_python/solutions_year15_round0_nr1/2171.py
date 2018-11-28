f = open("people2.txt", 'r')

tests = int(f.readline())

for i in range(0, tests):
  line = f.readline()
  parts = line.split(" ")
  num_peeps = int(parts[0])
  peeps = parts[1]
  clappers = 0
  needed = 0
  #print("Case #" + str(i + 1))

  for x in range(0, num_peeps + 1):
    shy = int(peeps[x])
    #print("shy = " + str(shy) + " clappers = " + str(clappers) + " needed = " + str(needed))
    if clappers >= x:
      clappers = clappers + shy
    elif shy > 0:
      needed = needed + (x - clappers)
      clappers = clappers + shy + (x-clappers)

  print("Case #" + str(i + 1) + ": " + str(needed))
