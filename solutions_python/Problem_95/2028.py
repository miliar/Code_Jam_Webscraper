d = {}
d["a"]="y"
d["b"]="h"
d["c"]="e"
d["d"]="s"
d["e"]="o"
d["f"]="c"
d["g"]="v"
d["h"]="x"
d["i"]="d"
d["j"]="u"
d["k"]="i"
d["l"]="g"
d["m"]="l"
d["n"]="b"
d["o"]="k"
d["p"]="r"
d["q"]="z"
d["r"]="t"
d["s"]="n"
d["t"]="w"
d["u"]="j"
d["v"]="p"
d["w"]="f"
d["x"]="m"
d["y"]="a"
d["z"]="q"
d[" "]=" "
d["\n"]=""


def translate(line):
	googlese = []
	for char in line:
		googlese.append(d[char])
	return ''.join(googlese)
	
if __name__ == "__main__":
	import sys
	file = open(sys.argv[1],'r')
	numTests = file.readline()
	for case in range(int(numTests)):
		string = "Case #"+str(case+1)+": "+translate(file.readline())
		string = string.rstrip()
		string = string.lstrip()
		print string
		
		
		