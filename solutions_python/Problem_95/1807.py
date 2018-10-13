f = file("test.txt", "r")
fout = file("output.txt", "w")
input = f.read().split("\n");
myString = ""

trans = {}
trans["a"] = "y"
trans["b"] = "h"
trans["c"] = "e"
trans["d"] = "s"
trans["e"] = "o"
trans["f"] = "c"
trans["g"] = "v"
trans["h"] = "x"
trans["i"] = "d"
trans["j"] = "u"
trans["k"] = "i"
trans["l"] = "g"
trans["m"] = "l"
trans["n"] = "b"
trans["o"] = "k"
trans["p"] = "r"
trans["q"] = "z"
trans["r"] = "t"
trans["s"] = "n"
trans["t"] = "w"
trans["u"] = "j"
trans["v"] = "p"
trans["w"] = "f"
trans["x"] = "m"
trans["y"] = "a"
trans["z"] = "q"
trans[" "] = " "



tests = int(input[0]) 
case = 1
while case <= tests:
	output = ""
	for i in input[case]:
		output += trans[i]
		

	myString += "Case #%d: %s\n" % (case, output)
	case += 1





print(myString)
fout.write(myString)