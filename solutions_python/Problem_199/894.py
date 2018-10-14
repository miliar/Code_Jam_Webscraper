def parseInputFrom(line):
  spl = line.split(" ")
  faces = 0
  for idx, x in enumerate(spl[0]):
    if x != "+":
      faces += 1 << idx
  size = int(spl[1])
  return faces, size

def solve(faces, size):
  n = 0
  m = (1 << size) - 1
  while faces >= m and n < 10:
    faces = faces ^ (m << faces.bit_length() - size)
    n += 1
  if faces == 0:
    return n
  return None

def represent(i, res):
  return "Case #"+str(i)+": "+("IMPOSSIBLE" if res is None else str(res))

with open("input.1.in") as f:
  with open("output.1.txt", "w") as f2:
    n = int(f.readline())
    i = 1
    line = f.readline()
    while line and i <= n:
      print(i, "/", n)
      faces, size = parseInputFrom(line)
      res = solve(faces, size)
      f2.write(represent(i, res)+"\n")
      i += 1
      line = f.readline()
