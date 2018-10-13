import string,sys

x = string.maketrans("qzejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv","zqourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup")

fn = sys.argv[1]
f  = open(fn, 'r')

n = f.readline()
i = 1
for line in f:
  print "Case #%d: %s" % (i, (line.rstrip()).translate(x))
  i = i+1

f.close()
