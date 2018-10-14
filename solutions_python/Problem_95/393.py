A = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyqez"
B = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupazoq"

def testCase(reversemap):
	line = raw_input().strip()
	return "".join(reversemap.get(ch, ch) for ch in line)

if __name__ == '__main__':
	reversemap = {}

	for a, b in zip(A, B):
		reversemap[a] = b
		reversemap[a.upper()] = b.upper()

	n = int(raw_input())
	for i in xrange(n):
		print "Case #%d: %s" % (i+1, testCase(reversemap))
