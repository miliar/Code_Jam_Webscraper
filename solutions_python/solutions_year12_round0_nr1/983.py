map_table_list = "ay bh ce ds eo fc gv hx id ju ki lg ml nb ok pr rt sn tw uj vp wf xm ya zq qz".split()
map_table = dict()
for x in map_table_list:
	map_table[x[0]] = x[1]
map_table[' '] = ' '


T = int(input())
#text = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"
#tran = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"
#maps = dict()
for t in range(T):
	print("Case #" + str(t+1), end=": ")
	text = input()
	for c in text:
		print(map_table[c], end='')
	print("")
