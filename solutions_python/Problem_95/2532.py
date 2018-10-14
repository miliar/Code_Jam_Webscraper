import string
o = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz"
n = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq"
tran = string.maketrans(o,n)
for i in range(int(raw_input())):
    print "Case #%d: %s" %(i + 1, (raw_input().translate(tran)))
