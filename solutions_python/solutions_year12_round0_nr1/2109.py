import string

conversion = string.maketrans("zyeqejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv", "qaozourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup")

with open("input") as fp:
	with open("output", "w") as out_file:
		# skip count
		fp.readline()

		output_lines = []
		for index, line in enumerate(fp.readlines()):
			out_file.write("Case #%s: %s" % (index+1, string.translate(line, conversion)))

