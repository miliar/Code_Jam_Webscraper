import string

T = int(raw_input())

# abcdefghijklmnoprstuvwxy | qz
# yhesocvxduiglbkrtnwjpfma | zq

alph = "abcdefghijklmnopqrstuvwxyz"
val =  "yhesocvxduiglbkrztnwjpfmaq"

for i in range(T):
    t = raw_input()
    ans = t.translate(string.maketrans(alph, val))
    print "Case #%d: %s" % (i+1, ans)
