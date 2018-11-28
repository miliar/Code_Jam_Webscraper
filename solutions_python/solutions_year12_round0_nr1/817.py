#!/usr/bin/python
import sys

ciphered  = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq"
cleartext = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz"

def build_dict():
	dict = {}
	for i in xrange(len(ciphered)):
		ciphered_letter = ciphered[i]
		clear_letter = cleartext[i]
		if (ciphered_letter in dict):
			clear_from_dict = dict[ciphered_letter]
			if (clear_from_dict != clear_letter):
				print "Error"
				sys.exit(1)
		else:
			dict[ciphered_letter] = clear_letter
	return dict
	
def main():
	dict = build_dict()
	T = int(sys.stdin.readline())
	
	for i in xrange(T):
		line = sys.stdin.readline().strip()
		message = ''
		for j in xrange(len(line)):
			message += dict[line[j]]
	
		print "Case #" + str(i+1) + ": " + message
main()
