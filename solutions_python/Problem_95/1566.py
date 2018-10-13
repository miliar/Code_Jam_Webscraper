mm="yhesocvxduiglbkrztnwjpfmaq"

n=input()
for i in range(n) :
    s=raw_input()
    s2=""
    for c in s :
        if c==' ' :
            s2+=' '
        else :
            s2+=mm[ord(c)-ord('a')]
    print "Case #%d:"%(i+1),s2