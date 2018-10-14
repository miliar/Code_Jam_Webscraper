import string
raw_input()
lambda s : string.translate(s, string.maketrans("ynficwlbkuomxsevzpdrjgthaq", "abcdefghijklmnopqrstuvwxyz"))
for i in enumerate(__import__("sys").stdin.read().splitlines()):
    print ("Case #%s" %(i[0]+1)) + ":", (lambda s : string.translate(s, string.maketrans("ynficwlbkuomxsevzpdrjgthaq", "abcdefghijklmnopqrstuvwxyz")))(i[1])
