from string import split
from math import copysign

def parse(filename):
  f = open(filename, 'r')
  t = int(f.readline()[:-1])
  data = []
  for iline in range(t):
    line = split(f.readline()[:-1])
    line.reverse()
    c = int(line.pop())
    combs = []
    for i in range(c):
      combs.append(line.pop())
    d = int(line.pop())
    opp = []
    for i in range(d):
      opp.append(line.pop())
    invoke = line[0]
    data.append((invoke, combs, opp))
  f.close()
  return data

def main(fileprefix):
  data = parse(fileprefix + '.in')
  f = open(fileprefix + '.out', 'w')
  i = 1;
  for trial in data:
    export('Case #{0:d}: {1:s}'.format(i, calc(trial)), f)
    i += 1;
  f.close()

def export(str, file):
  print str
  file.write(str + '\n')

def calc(data):
  (invoke, comb, neg) = data
  comb = triecomb(comb)
  neg = trieneg(neg)
  elemlist = []
  for spell in invoke:
    # See if combine
    if elemlist and spell in comb.keys() and elemlist[-1] in comb[spell].keys():
      spell = comb[spell][elemlist[-1]]
      elemlist.pop()
    # See if negate
    if spell in neg.keys() and any([n in elemlist for n in neg[spell]]):
      elemlist = []
    else:
      elemlist.append(spell)
  return tostring(elemlist)

def trieneg(neg):
  trie = {}
  for pair in neg:
    if not pair[0] in trie.keys():
      trie[pair[0]] = [pair[1]]
    else:
      trie[pair[0]].append(pair[1])
    if not pair[1] in trie.keys():
      trie[pair[1]] = [pair[0]]
    else:
      trie[pair[1]].append(pair[0])
  return trie

def triecomb(comb):
  trie = {}
  for trip in comb:
    if not trip[0] in trie.keys():
      trie[trip[0]] = {trip[1]:trip[2]}
    else:
      trie[trip[0]][trip[1]] = trip[2]
    if not trip[1] in trie.keys():
      trie[trip[1]] = {trip[0]:trip[2]}
    else:
      trie[trip[1]][trip[0]] = trip[2]
  return trie

def tostring(elemlist):
  out = ''
  for spell in elemlist:
    out += spell + ', '
  return '[' + out[:-2] + ']'

