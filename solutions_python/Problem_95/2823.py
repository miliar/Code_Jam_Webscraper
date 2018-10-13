map = dict()
map["y"] = "a"
map["n"] = "b"
map["f"] = "c"
map["i"] = "d"
map["c"] = "e"
map["w"] = "f"
map["l"] = "g"
map["b"] = "h"
map["k"] = "i"
map["u"] = "j"
map["o"] = "k"  
map["m"] = "l"
map["x"] = "m"
map["s"] = "n"
map["e"] = "o"
map["v"] = "p"
map["z"] = "q"
map["p"] = "r"
map["d"] = "s"
map["r"] = "t"
map["j"] = "u"
map["g"] = "v"
map["t"] = "w"
map["h"] = "x"
map["a"] = "y"
map["q"] = "z"

import sys

def replace(str):
	r = ""
	for c in str:
		if (c == '\n'):
			continue
		if (c == " "):
			r = r + c
		else:
			r = r + map[c]

	return r

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(t):
        a = f.readline()
        
        print "Case #%d: %s" % (_t+1, replace(a))