# Google Code Jam Template

i = open("A-small-attempt0.in", "r")
o = open("A-small.out", "w")

T = int(i.readline())
PI = 3.14159265359

def ringarea(R, r):
  return (R + r)*(R - r)

for c in range(1, T + 1):
    r, t = map(int, i.readline().replace('\n','').split())

    used = 0
    y = 0
    rA = r
    rB = r + 1
    while used < t:
      used += ringarea(rB, rA)
      y += 1
      rA = rB + 1
      rB = rB + 2
      if used + ringarea(rB, rA) > t:
        break
    

    # do stuff
    result = y

    o.write("Case #{0}: {1}\n".format(c, result))

i.close()
o.close()