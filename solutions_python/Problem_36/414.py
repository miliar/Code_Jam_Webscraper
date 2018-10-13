#! /usr/bin/env python

def substrings(str, substr):
	def substr_recursive(str, substr):
		if len(substr) == 0:
			return 1

		count = 0
		letter = substr[0]

		index = str.find(letter)

		while index != -1:
			str = str[index + 1:]
			count = count + substr_recursive(str, substr[1:])

			index = str.find(letter)

		return count

	return 0 + substr_recursive(str, substr)

cases = int(raw_input())

for c in range(cases):
	string = raw_input()

	strings = str(substrings(string, "welcome to code jam"))[-4:]
	print "Case #%d: %s" % (c + 1, strings.zfill(4))
