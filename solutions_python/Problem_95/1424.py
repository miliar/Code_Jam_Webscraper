cvs = "ynficwlbkuomxsevzpdrjgthaq"
f = open("asmall.in", "r")
l = f.readlines()

def cv(x):
    if x == ' ': return x
    else:
        return chr(97+cvs.find(x))

cnt = 1
for st in l[1:]:
    if len(st.strip()) == 0:
        break
    print "Case #%d:" % cnt, "".join(map(cv, st.strip()))
    cnt += 1
