import sys, string

charmap = string.maketrans("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z", "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q")

count = sys.stdin.readline();

case = 0;

for line in sys.stdin:
	case += 1
	print "Case #" + str(case) + ": " + line.strip().translate(charmap)
