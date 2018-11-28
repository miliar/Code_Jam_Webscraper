d = {}
d["a"] = "y"
d["b"] = "h"
d["c"] = "e"
d["d"] = "s"
d["e"] = "o"
d["f"] = "c"
d["g"] = "v"
d["h"] = "x"
d["i"] = "d"
d["j"] = "u"
d["k"] = "i"
d["l"] = "g"
d["m"] = "l"
d["n"] = "b"
d["o"] = "k"
d["p"] = "r"
d["q"] = "z"
d["r"] = "t"
d["s"] = "n"
d["t"] = "w"
d["u"] = "j"
d["v"] = "p"
d["w"] = "f"
d["x"] = "m"
d["y"] = "a"
d["z"] = "q"
d[" "] = " "

def transforma(cad):
	nueva = ""
	for car in cad:
		nueva += d[car]
	return nueva

f = open("file.in", "r")
s = open("output", "w")

f.readline()
contador = 1
for linea in f:
	s.write("Case #%d: %s\n" % (contador, transforma(linea[:-1])))
	contador += 1
f.close()
s.close()
