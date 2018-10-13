import sys
import os

mapping = {}
train = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
train = filter(lambda x: 'a'<=x<='z', train)
trainouts = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
trainouts = filter(lambda x: 'a'<=x<='z', trainouts)
mapping = dict(zip(train,trainouts))
mapping['y'] = 'a'
mapping['e'] = 'o'
mapping['q'] = 'z'
mapping['z'] = 'q'

'''s = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
aej vkddci eww rbc fbkfocs myia
mcr mkvd ie tbyr bysid ie
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
aej tysr dcmm rbksld yr xc neksl qeeex
ejp feic uyx kd mkoc rbc varbylepcys rbcepcx
rbcpc kd se ysdtcp
w ew rte czjymd w ew esc czjymd esc
wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
rbyso aej njr rbc pcym leelmcpcdc kd ks yserbcp fydrmc
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
bet ypc aej bemiksl jv ncfyjdc kx y veryre
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
ys cac wep ys cac ysi y vklces wep y vklces""".split('\n')'''
s="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
aej vkddci eww rbc fbkfocs myia
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
bet ypc aej bemiksl jv ncfyjdc kx y veryre
ejp feic uyx kd mkoc rbc varbylepcys rbcepcx
rbcpc kd se ysdtcp
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd
aej tysr dcmm rbksld yr xc neksl qeeex""".split('\n')
import re
l = [re.sub("([a-z])", lambda x: mapping[x.groups(1)[0]], each) for each in s]
i = 1
for each in l:
	print "Case #%d: %s" % (i, each)
	i += 1

