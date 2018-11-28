lang = """clsyvfaxta
sxqzcxgpav
xwwsvifbrh
vvuptrxwoq
yiopjsoqho
ngkkygsfjl
mgjiwczvap
lzazqjrezb
unhfzintny
fceqmcumxv
dlwdmmpesq
hmdqtcaiyo
gdsnverpsr
mwcibowquo
hbdmuyruhp
kpucephwgb
ntxrbbfatc
qcfvpzuiwb
zgsvlxksts
viltzpwgpp
ihuodlpxtn
auusphpbbk
twufrvuncl
fmuzcxkuwf
hybdrqkirl""".split("\n")

cases="""vmiprzlnpp
m(inpw)cibowquo
(rta)(vjl)(xe)(oru)(rve)(vzc)(ipv)(opv)(zjp)(zde)
(mnae)(mtcg)(xejv)(hisz)(qwxh)(chip)(zdmn)(kvwj)(oram)(vcdp)
(rstuvwxyzabcdefghiklmnopq)(abcdefghjklmnopqrstuvxyz)(uvwxyzacefghijklmnopqrt)(prstuvwxyzabcdefghijno)(tvwxyzabcdegijklnopqr)(ghijklmnoqrstuvwxyzabdef)(bdfghijklmnopqstuvwxya)(bdefghijlmnopqrtuvwxyz)(jkmnoqrstvwxyadefghi)(yacdefghijklmorstuvwx)
(oqstuvwxyzbcdefghijlm)(fghijklmoqrstuvwxyzabcde)(uwxyabcdefghjkmnoprst)(ijkmnopqruwxyabcdefgh)(lmnopqrstuwxyzabcdefgij)(klnpqrstuvwxyzabdfgij)(ijklmnoqrsuvwxyzacdefg)(jklmnopqrstuvwxyzabcdefghi)(ghijmnpqrstuvxyabcdef)(abcdefgijlmopqstuvwxyz)
(fsc)(losy)(fsx)(yltw)(rvbf)(fmpr)(pak)(klrx)(ycst)(uagm)
(defghiklnpqrstuwxyzac)(noprstwxyabcdefghijklm)(klmnopqrstuvwxabdefgj)(mnopqstuvxyzabcdfghikl)(fghijklmnorsuvwyzabcde)(uwxyzabcdefhijkmnopqrst)(qrstvwzbdefghjlmnop)(defghijmnoqrstvwxzab)(qrstuvwxzacdfghijklmnop)(wyzbcdefghijklmnopqrstuv)
(orvx)(vyel)(kuah)(psuf)(tmnp)(veor)(hxzb)(vwmp)(gnow)(qyak)
(stuvxyabcdefghiklmnpqr)(xyzacdefghklmopqrtuvw)(fghijklmnoqrstvwxyabcde)(cdfghijkmnoqstuvwxyzab)(nopqrtuvwxyzabfgijlm)(yabcdefghijklmnopqrstvwx)(mnpqrsuvwxzadeghijkl)(pqrstvwxyzbcdegikln)(xyabdefghklnopqrstvw)(qrstuwxyzabcdefghjklmno)""".split("\n")


d=set([""])

for w in lang:
    for i in range(1,len(w)+1):
        d.add(w[:i])
print d



L=len(lang[0])

def c(w, i=0, pre=""):
    if pre not in d:
        return 0
    if i==L:
        #print pre
        return 1
    return sum(c(w, i+1, pre+l) for l in w[i])

t=1        
for word in cases:
    w = []
    sub=False
    temp=[]
    for l in word:
        if l=='(':
            sub=True
        elif l==')':
            sub=False
            w.append(temp)
            temp=[]
        else:
            
            if sub:
                temp.append(l)
            else:
                w.append([l])
    print "Case #%d: %d" % (t, c(w))
    t+=1
                

