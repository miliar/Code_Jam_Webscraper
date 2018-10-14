from string import maketrans

googlerese = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz"
english = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq"

trans = maketrans(googlerese, english)

T = int(raw_input())
for case in xrange(T):
    print "Case #%s: %s" %(case+1, raw_input().translate(trans))
