dictionary = {
	"a" : "y",
	"b" : "h",
	"c" : "e",
	"d" : "s",
	"e" : "o",
	"f" : "c",
	"g" : "v",
	"h" : "x",
	"i" : "d",
	"j" : "u",
	"k" : "i",
	"l" : "g",
	"m" : "l",
	"n" : "b",
	"o" : "k",
	"p" : "r",
	"q" : "z",
	"r" : "t",
	"s" : "n",
	"t" : "w",
	"u" : "j",
	"v" : "p",
	"w" : "f",
	"x" : "m",
	"y" : "a",
	"z" : "q"
}

input_file_lines = open("A-small-attempt2.in").readlines()
del input_file_lines[0]

for line_number, line in enumerate(input_file_lines):
	result = "Case #" + str(line_number + 1) + ": "
	for letter in list(line):
		try:
			result += " " if letter == " " else dictionary[letter]
		except KeyError:
			pass
	print result
