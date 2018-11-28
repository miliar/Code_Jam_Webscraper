def deceitful(n, nBlocks, kBlocks):
  ''' return number of points naomi will score if she plays OPT dWar '''
  # naomi's strategy: "tell" largest possible block, then pick min block
  # that beats ken's min block. if his block is bigger, pick min block.
  # ken's strategy: pick min block - either to win round, or to save big
  # blocks

  # you say you're using big, so ken wil pick small - when he does, you pick
  # the smallest block that will still win the round

  # eg always say you have .99x and when he plays his smallest block, you
  # play your next highest block above his smallest block
  wins = 0

  for rnd in xrange(n):
    kMin = min(kBlocks)

    # get all elements greater than kMin
    gt_kMin = [ ]
    for e in nBlocks:
      if e > kMin:
        gt_kMin.append(e)

    # if there's at least one elt greater than kMin, use that block to weigh
    # otherwise, discard the lightest remaining block in naomi's set
    if len(gt_kMin) > 0:
      wins += 1
      nMin = min(gt_kMin)
    else:
      nMin = min(nBlocks)

    kBlocks.remove(kMin)
    nBlocks.remove(nMin)

  return wins


def truthful(n, nBlocks, kBlocks):
  ''' return number of points naomi will score if she plays OPT tWar '''
  # ken's strategy: pick smallest block that will still win round, or min
  # block if can't win
  # naomi's strategy: pick largest block
  wins = 0

  for rnd in xrange(n):
    nMax = max(nBlocks)

    # get all elements greater than nMax
    gt_nMax = [ ]
    for e in kBlocks:
      if e > nMax:
        gt_nMax.append(e)

    # if there's at least one elt greater than nMax, use that block to weigh
    # otherwise, discard the lightest remaining block in naomi's set
    if len(gt_nMax) is 0:
      wins += 1
      kMin = min(kBlocks)
    else:
      kMin = min(gt_nMax)

    kBlocks.remove(kMin)
    nBlocks.remove(nMax)

  return wins


def solve(fname):
  output = open("output4.txt", "w+")
  with open(fname, "r") as f:
    numCases = int(f.readline())

    for i in xrange(numCases):
      numBlocks = f.readline()

      naomiBlocks = [ float(x) for x in f.readline().split(" ") ]
      kenBlocks = [ float(x) for x in f.readline().split(" ") ]

      dWar = deceitful(len(naomiBlocks), list(naomiBlocks), list(kenBlocks))
      tWar = truthful(len(naomiBlocks), list(naomiBlocks), list(kenBlocks))

      output.write("Case #{}: {} {}\n".format(i+1, dWar, tWar))

# solve("input4.txt")
solve("input4.in")

