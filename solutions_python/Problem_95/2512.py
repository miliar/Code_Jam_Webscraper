from string import maketrans

goog = 'abcdefghijklmnopqrstuvwxyz'
real = 'ynficwlbkuomxsevzpdrjgthaq'
tran = maketrans(real, goog)

cases = open('A-small-attempt0.txt', 'r').read().split("\n")[1:]
for case in range(len(cases)):
    print "Case #" + str(case + 1) + ": " + cases[case].translate(tran)
