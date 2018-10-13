#!/usr/bin/env python
#-*- coding: utf-8 -*- 
import sys
from string import ascii_lowercase

def find_missed_chars(dict_translation, lang):
	"""Locate the chars for a language that are not in the dictionary"""
	lst_chars = list(ascii_lowercase)
	for s in ascii_lowercase:
		if lang == 'googlerese':
			if s in dict_translation:
				lst_chars.remove(s)
		elif lang == 'english':
			if s in dict_translation.values():
				lst_chars.remove(s)
	print lst_chars

def translate(str_googlerese, dict_translation):
	result = ""
	for c in str_googlerese:
		if c in ascii_lowercase:
			result += dict_translation[c]
		else:
			result += c
	return result

if __name__ == '__main__':
	str_googlerese = """ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"""
	str_english =    """ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"""
	dict_translation = {'z':'q', 'q':'z', ' ':' '}
	for idx, char_goo in enumerate(str_googlerese):
		if char_goo.isalpha():
			dict_translation[char_goo] = str_english[idx]
	#find_missed_chars(dict_translation, 'googlerese')
	#find_missed_chars(dict_translation, 'english')
	f = open (sys.argv[1], 'r')
	test_cases = int(f.readline())
	for i in range(test_cases):
		case = f.readline()
		print "Case #%i: %s" %(i + 1, translate(case, dict_translation)),