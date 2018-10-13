data = [l.strip() for l in open("infile", "r").readlines()]
out = open("outfile", "w")  

class element:
  def __init__(self, e):
    self.el = e
    self.combs = {}
    self.opps = []

ncases = int(data.pop(0))
for case in range(ncases):
  casedata = data.pop(0).split(' ')
  # set up data structure
  els = {}
  for i in range(0, 26):
    char = chr(i + 65)
    els[char] = element(char)
  # populate
  numcombs = int(casedata.pop(0))
  for i in range(numcombs):
    comb = casedata.pop(0)
    els[comb[0]].combs[comb[1]] = comb[2]
    els[comb[1]].combs[comb[0]] = comb[2]
  numopps = int(casedata.pop(0))
  for i in range(numopps):
    opp = casedata.pop(0)
    els[opp[0]].opps.append(opp[1])
    els[opp[1]].opps.append(opp[0])
  numinvocations = int(casedata.pop(0))
  invstring = casedata.pop(0)
  invindex = 0
  thelist = []
  while invindex < numinvocations:
    inv = invstring[invindex]
    thelist.append(inv)
    if len(thelist) < 2:
      pass
    else:
      if thelist[-1] in els[thelist[-2]].combs:
        newel = els[thelist[-2]].combs[thelist[-1]]
        thelist.pop(-1)
        thelist.pop(-1)
        thelist.append(newel)        
      else:
        # check for oppositions
        myopps = els[inv].opps
        for e in thelist[:-1]:
          if e in myopps:
            thelist = []
            break
    invindex += 1
  # convert to correct output form
  outline = "["
  for i in thelist:
    outline += i + ", "
  if outline[-1] == ' ':
    outline = outline[:-2]
  outline += "]"
  out.write("Case #" + str(case+1) + ": " + outline + "\n")
   
