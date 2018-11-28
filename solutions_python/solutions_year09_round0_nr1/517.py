#! /usr/bin/env python

import string

def perms(lists):
	def perms_recursive(prefix, lists):
		if len(lists) == 0:
			yield prefix
		else:
			for char in lists[0]:
				for w in perms_recursive(prefix + char, lists[1:]):
					yield w

	for w in perms_recursive("", lists):
		yield w

def check_words(word, groups):
	is_word = True

	for i in range(len(word)):
		if not word[i] in groups[i]:
			is_word = False

			break

	return is_word

def parse_line(line):
	i = 0
	groups = []

	while i < len(line):
		if line[i] == '(':
			close_pos = i + string.find(line[i:], ')')

			groups.append(list(line[i + 1:close_pos]))

			i = close_pos + 1
		else:
			groups.append([line[i]])

			i = i + 1

	return groups

def count_words(word_list, groups):
	count = 0

	for w in word_list:
		if check_words(w, groups):
			count = count + 1

	return count

word_list = []

params = raw_input().split(' ')
params = [int(x) for x in params]

[letters, words, cases] = params

for i in xrange(words):
	word_list.append(raw_input())

for i in xrange(cases):
	line = raw_input()

	groups = parse_line(line)

	print "Case #%d: %d" % (i + 1, count_words(word_list, groups))
	 
