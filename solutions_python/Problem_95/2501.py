import sys, string

english = "abcdefghijklmnopqrstuvwxyz"
googlerese = "ynficwlbkuomxsevzpdrjgthaq"
trans_table = string.maketrans(googlerese, english)

num_cases = int(sys.stdin.readline())
for i in xrange(num_cases):
    cipher = sys.stdin.readline().strip()
    plaintext = cipher.translate(trans_table)
    print "Case #%d: %s" % (i + 1, plaintext)
