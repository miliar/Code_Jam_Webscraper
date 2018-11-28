from __future__ import division
import sys
sys.setrecursionlimit(1500)

def B(N, Colors):
  if any([c > N/2 for c in Colors]):
    return "IMPOSSIBLE"
  names = [c for c in "ROYGBV"]
  tuples = [{"count":Colors[i], "name":names[i]} for i in range(0,6)]
  result = BRecurse(tuples, "", "")
  if result[0] != result[-1]:
    return result
  return FixLast(result)

def FixLast(result):
  last = result[-1]
  result = result[0:-1]
  for i in range(0,len(result)):
    if result[i] != last and result[i+1] != last:
      return result[:(i+1)] + last + result[(i+1):]
  return "IMPOSSIBLE"

def BRecurse(colors, last, sofar):
  colors.sort(key=lambda x: x["count"], reverse=True)
  if colors[0]["count"] == 0:
    return sofar
  if colors[0]["name"] != last:
    colors[0]["count"] -= 1
    return BRecurse(colors, colors[0]["name"], sofar+colors[0]["name"])
  if colors[1]["count"] == 0:
    return "IMPOSSIBLE"  
  colors[1]["count"] -= 1
  return BRecurse(colors, colors[1]["name"], sofar+colors[1]["name"])


def Parse():
  fin = open(r"D:\Projects\Python\Google\Round1B\B-small-attempt0.in", 'r')
  fout = open(r"D:\Projects\Python\Google\Round1B\B-small-attempt0.out", 'w')
  count = int(fin.readline())
  for i in range(1, count+1):
    line = [int(s) for s in fin.readline().split(" ")]
    N = line[0]
    Colors = line[1:]
    ret = B(N, Colors)
    result = "Case #%d: %s\n" % (i, ret)
    print result
    fout.write(result)
  fin.close()
  fout.close()

Parse()