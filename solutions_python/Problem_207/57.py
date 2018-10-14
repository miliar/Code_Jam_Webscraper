import sys

if __name__ == "__main__":
  data = open(sys.argv[1]).readlines()
  t = int(data[0])
  for i in range(1, t+1):
    row = [int(x) for x in data[i].split(" ")]
    if max(row[1:]) > row[0]/2:
      print("Case #%d: IMPOSSIBLE" % i)
      continue
    vals = [None] * row[0]
    colors = "ROYGBV"
    tmp = [[n, c] for c,n in zip(colors, row[1:])]
    tmp = sorted(tmp)[::-1]
    s = ""
    for j in tmp:
      s += j[1] * j[n]
    idx = 0
    for ch in s:
      if idx >= len(vals):
        idx = 1
      vals[idx] = ch
      idx += 2
    print("Case #%d: %s" % (i, "".join(vals)))
    
