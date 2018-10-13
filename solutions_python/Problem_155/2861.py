lines = [l for l in open("A-large.in")]
cases = int(lines[0])

def ovation(maxshy, audience):
  standing = 0
  for (idx, v) in enumerate(audience):
    if standing >= idx:
      standing += v
  return standing

for i in range(1, cases + 1):
  maxshy = int(lines[i].split(" ")[0])
  audience = [int(c) for c in lines[i].split(" ")[1].strip()]
  
  standing = ovation(maxshy, audience)
  friends = 0
  while standing < sum(audience):
    audience[0] += 1
    friends += 1
    standing = ovation(maxshy, audience)
  
  print("Case #%d: %d" % (i, friends))