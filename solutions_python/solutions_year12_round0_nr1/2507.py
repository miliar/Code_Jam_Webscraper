from string import maketrans

translate_from = "abcdefghijklmnopqrstuvwxyz"
translate_to = "ynficwlbkuomxsevzpdrjgthaq"

t = maketrans(translate_to, translate_from)
with open("A-small-attempt0.in", "r") as f:
    for i, line in enumerate(f):
        if i == 0:
            pass 
        else:
            sentence = line.strip("\n")
            print "Case #%s: %s" % (str(i), sentence.translate(t))
