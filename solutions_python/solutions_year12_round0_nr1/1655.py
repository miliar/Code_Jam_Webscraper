#/bin/python
from sys import stdin
from string import maketrans

sample_in  = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq" 
sample_out = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz"

m = {}
for a,b in zip(sample_in, sample_out):
  m[a]=b

#print len(m.keys())

t = maketrans("".join(m.keys()), "".join(m.values()))
r = stdin.readlines()
N = r.pop(0)
for i,s in enumerate(r):
  print "Case #%d: %s" % (i+1, s.strip().translate(t))


