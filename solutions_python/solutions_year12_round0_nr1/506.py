from string import maketrans
T = int(input())+1
for t in range(1,T):
    print "Case #%d:" % t, raw_input().translate(maketrans("ynficwlbkuomxsevzpdrjgthaq","abcdefghijklmnopqrstuvwxyz"))