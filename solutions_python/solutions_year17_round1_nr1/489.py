def solve(arr):
  for r in xrange(len(arr)):
    row = arr[r]
    hasElem = False
    for e in row:
      if e != '?':
        hasElem = True
        break
    if hasElem:
      i = 0
      fillBegin = True
      last = None
      while i < len(row):
        if row[i] != '?':
          if fillBegin:
            nowI = i - 1
            while nowI >= 0:
              row[nowI] = row[i]
              nowI -= 1
          fillBegin = False
          last = row[i]
        else:
          row[i] = last
        i += 1
  for r in xrange(len(arr)):
    row = arr[r]
    hasElem = False
    for e in row:
      if e != '?':
        hasElem = True
        break
    if not hasElem:
      row = arr[r]
      rNow = r
      ii = 1
      while True:
        if rNow - ii >= 0 and arr[rNow - ii][0] != '?':
          rowToCopy = rNow - ii
          break
        if rNow + ii < len(arr) and arr[rNow + ii][0] != '?':
          rowToCopy = rNow + ii
          break
        ii += 1

      for i in xrange(len(row)):
        row[i] = arr[rowToCopy][i]
  return arr

if __name__ == "__main__":
  T = input()
  for t in xrange(T):

    R, C = map(int, raw_input().split(" "))
    arr = []
    for r in xrange(R):
      arr.append(list(raw_input()))
    print "Case #" + str(t + 1) + ":"
    a = solve(arr)
    for i in a:
      print "".join(i)
