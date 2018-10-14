def processCake(cake):
    firstNonEmptyRow = -1
    for i in xrange(len(cake)):
        row = cake[i]
        firstQ = -1
        lastLetter = -1
        foundLetter = False
        for j in xrange(len(row)):
            currLetter = row[j]
            if(currLetter == "?"):
                if(firstQ == -1):
                    firstQ = j
            else:
                lastLetter = j
                foundLetter = True
                if(firstQ != -1):
                    temp = [currLetter] * (j - firstQ)
                    row = row[:firstQ] + temp + row[j:]
                    firstQ = -1
        cake[i] = row
        if(foundLetter):
            if(firstNonEmptyRow == -1):
                firstNonEmptyRow = i
            if(lastLetter < len(row) -1):
                lastChr = row[lastLetter]
                temp = [lastChr] * (len(row) - lastLetter - 1)
                cake[i][lastLetter + 1:] = temp
        elif(i > 0):
            cake[i] = cake[i-1]
    # fill starting empty rows
    fill = cake[firstNonEmptyRow]
    for i in xrange(firstNonEmptyRow):
        cake[i] = fill

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# input
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  R, C = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  cake = []
  for row in xrange(R):
    currInput = raw_input()
    currRow = []
    for j in xrange(len(currInput)):
        currRow.append(currInput[j])
    cake.append(currRow)
  processCake(cake)
  # output
  print "Case #{}:".format(i)
  for row in cake:
    print "".join(row)

  # print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options