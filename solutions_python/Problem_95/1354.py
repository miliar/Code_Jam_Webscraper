import string
import sys

trans = string.maketrans("qzejp myslckdxvnribtahwfoug", "zqour langeismpbtdhwyxfckjv")

sys.stdin.next()
for i, line in enumerate(sys.stdin):
    print "Case #{0}: {1}".format(i+1, line.rstrip().translate(trans))
