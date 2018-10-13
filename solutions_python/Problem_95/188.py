input="""\
30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
aej vkddci eww rbc fbkfocs myia
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
ys cac wep ys cac ysi y vklces wep y vklces
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
"""

input=input.strip().split('\n')
n=int(input[0])
data = input[1:n+1]


def swap(c,ass):
    if c in ass: return ass[c]
    else:
        return c.upper()

def swapstr(st,ass):
    s = ""
    for c in st:
        s+=swap(c,ass)
    return s

def do_assign(ass,s1,s2):
    a2=ass.copy()
    for i in range(len(s1)):
        if not s1[i] in a2:
            a2[s1[i]] = s2[i]
    return a2



a0="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

a1="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

a0 = a0.replace(' ','').replace('\n','')
a1 = a1.replace(' ','').replace('\n','')

ass = {}
ass = do_assign(ass,a0,a1)
ass = do_assign(ass,"qz","zq")

for i in range(1,n+1):
    print 'Case #%d:'%i,swapstr(input[i],ass)
    
