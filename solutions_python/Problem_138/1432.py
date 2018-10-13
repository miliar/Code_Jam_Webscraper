import copy

def war(naomi, ken):
  while min(naomi) < max(ken):
    kmax = max(ken)
    nplay = max(filter(lambda b : b < kmax, naomi))
    ken.remove(kmax)
    naomi.remove(nplay)
    if len(naomi) == 0:
      return 0
  return len(naomi)
  

def dwar(naomi, ken):
  winners = 0
  while min(ken) < max(naomi):
    kmin = min(ken)
    nchoices = filter(lambda b : b > kmin, naomi)
    if len(nchoices) == 0:
      return winners
    nplay = min(nchoices)
    ken.remove(kmin)
    naomi.remove(nplay)
    winners += 1
    if len(naomi) == 0:
      return winners
  return winners

in_file = open("D-large.in", "r")

t = int(in_file.readline())
ken = []
naomi = []

for i in xrange(t):
  n = int(in_file.readline())
  naomi.append(map(float, in_file.readline().split(' ')))
  ken.append(map(float, in_file.readline().split(' ')))

for i in xrange(t):
  n1 = copy.deepcopy(naomi[i])
  k1 = copy.deepcopy(ken[i])
  print "Case #%d: %d %d" % (i + 1, dwar(n1, k1), war(naomi[i], ken[i]))
