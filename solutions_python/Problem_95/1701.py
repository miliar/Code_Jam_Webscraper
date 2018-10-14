
dict = {}

in1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
in2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
in3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

o1 = "our language is impossible to understand"
o2 = "there are twenty six factorial possibilities"
o3 = "so it is okay if you want to just give up"

def mapper(instr, outstr):
    for i in xrange(0, len(instr)):
        if instr[i] != " ":
            #dict[outstr[i]] = instr[i]
            dict[instr[i]] = outstr[i]


mapper(in1, o1)
mapper(in2, o2)
mapper(in3, o3)

dict["z"] = "q"
dict["q"] = "z"


inp = """30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
bet ypc aej bemiksl jv ncfyjdc kx y veryre
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
mcr mkvd ie tbyr bysid ie
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
ys cac wep ys cac ysi y vklces wep y vklces
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
"""

inp = filter(None, inp.split("\n")[1:])

f = open("output", "w")

i = 1

for case in inp:
    tmp = ""
    for c in case:
        if c != ' ':
            tmp += dict[c]
        else:
            tmp += " "
    f.write("Case #%s: %s\n" % (i, tmp) )
    i+=1