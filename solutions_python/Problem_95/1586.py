googlerese_dict = {
	" ": " ",
	"a": "y",
	"b": "h",
	"c": "e",
	"d": "s",
	"e": "o",
	"f": "c",
	"g": "v",
	"h": "x",
	"i": "d",
	"j": "u",
	"k": "i",
	"l": "g",
	"m": "l",
	"n": "b",
	"o": "k",
	"p": "r",
	"q": "z",
	"r": "t",
	"s": "n",
	"t": "w",
	"u": "j",
	"v": "p",
	"w": "f",
	"x": "m",
	"y": "a",
	"z": "q"
}

def translate(line):
	res = ""
	for c in line:
		res+= googlerese_dict[c]
	return res

if __name__ == "__main__":

	input = file("A-small.in").read().strip().split('\n')
	output = open("A-small.out", "w")

	cases = int(input[0])
	for i in range(0, cases):
		output.write("Case #{0}: {1}\n".format(i+1, translate(input[i+1])))
	output.close()
