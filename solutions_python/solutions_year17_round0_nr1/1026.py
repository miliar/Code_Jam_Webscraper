f = open('A-large.in', 'r')
# f = open('A.txt', 'r')
out = open('A-large-out.txt', 'w')
ncases = f.readline()

def switch(c):
  if c=="-":
    return "+"
  if c=="+":
    return "-"

cases = f.readlines()
for i in range(len(cases)):
  done = False
  out.write("Case #%d: " %(i+1))
  pancakes, k = cases[i].split()
  pancakes = list(pancakes)
  k = int(k)
  if len(pancakes) < k:
    out.write("IMPOSSIBLE\n")
    done = True
  else:
    counter = 0
    for c in range(len(pancakes)):
      if pancakes[c] == "-":
        if c+k>len(pancakes):
          out.write("IMPOSSIBLE\n")
          done = True
          break
        else:
          for ci in range(c, c+k):
            pancakes[ci] = switch(pancakes[ci])
          counter +=1
    if not done:
      out.write(str(counter)+"\n")


