import sys
import re

def main():
	line = sys.stdin.readline();
	(L, D, N) = [int(i) for i in line.split()];

	words = []
	for i in range(D):
		line = sys.stdin.readline();
		words.append(line);

	for i in range(N):
		line = sys.stdin.readline();
		pattern = line.replace('(', '[').replace(')', ']');

		matches = 0;

		regex = re.compile(pattern);
		for word in words:
			if regex.match(word):
				matches += 1;

		print("Case #%d: %d" % (i + 1, matches));

main()
