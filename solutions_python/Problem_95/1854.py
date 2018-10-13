#!/usr/bin/env python
import sys

sin = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
sout = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

# Mapping for Googlerese to English. The letters "q" and "z" don't appear in
# either sample texts, and we are given "q" \mapsto "z".
goo_to_eng = {" " : " ", "q" : "z", "z" : "q"}

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	# Use sample to find the base mapping.
	for l in xrange(len(sin)):
		if sin[l] >= "a" and sin[l] <= "z" and sin[l] not in goo_to_eng:
			goo_to_eng[sin[l]] = sout[l]

	T = int(sys.stdin.readline())
	for t in xrange(T):
		G = sys.stdin.readline().rstrip("\n")
		translated = ""
		for g in G:
			translated += goo_to_eng[g]
			
		print "Case #%d: %s" % (t + 1, translated)

if __name__ == "__main__":
	sys.exit(main())

