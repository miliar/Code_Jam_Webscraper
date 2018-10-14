inputLang = 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv '
outpuLang = 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup '
language = dict()
language['\n']  = ''
language['z']  = 'q'
language['q']  = 'z'

for i, x in enumerate(inputLang):
	language[x] = outpuLang[i]

lines = open('A-small-attempt2.in', 'r').readlines()[1:]
for i, line in enumerate(lines):
	print 'Case #' + str(i+1) + ': ' + ''.join(map(lambda x: language[x], line))
