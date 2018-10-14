def process_strings(a, b, char_map):
	if len(a) != len(b):
		print "invalid strings"
		raise
	for i in range(0, len(a)):
		char_map[a[i]] = b[i]
	return char_map

def main():
	char_map = {"z":"q", "q":"z"}
	char_map = process_strings("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand", char_map)
	char_map = process_strings("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", char_map)
	char_map = process_strings("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up", char_map)
	input = open("A-small-attempt3.in", "r").readlines()
	T = int(input[0])
	for t in range(1, T + 1):
		output = []
		text = input[t].rstrip('\n')
		for ch in text:
			output.append(char_map[ch])
		print "Case #%d: %s" % (t, "".join(output))

if __name__ == "__main__":
	main()
