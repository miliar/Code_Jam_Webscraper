Python 2.5 (r25:51908, Sep 19 2006, 09:52:17) [MSC v.1310 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2      
>>> s = dict()
>>> d - dict()

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d - dict()
NameError: name 'd' is not defined
>>> d = dict()
>>> s = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
>>> d = "our language is impossible to understand"
>>> for (k, v) in zip(d, s):
	trans[k] = v

	

Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    trans[k] = v
NameError: name 'trans' is not defined
>>> trans = dict()
>>> for (k, v) in zip(d, s):
	trans[k] = v

	
>>> trans
{'a': 'y', ' ': ' ', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'i': 'k', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r'}
>>> s = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
>>> d = "there are twenty six factorial possibilities"
>>> for (k, v) in zip(d, s):
	trans[k] = v

	
>>> trans
{' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'y': 'a', 'x': 'h'}
>>> s = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
>>> 
>>> d = "so it is okay if you want to just give up"
>>> for (k, v) in zip(d, s):
	trans[k] = v

	
>>> len(trans)
25
>>> for i in xrange(ord("a"), ord("z")+1):
	print chr(i), trans[chr(i)]

	
a y
b n
c f
d i
e c
f w
g l
h b
i k
j u
k o
l m
m x
n s
o e
p v
q

Traceback (most recent call last):
  File "<pyshell#25>", line 2, in <module>
    print chr(i), trans[chr(i)]
KeyError: 'q'
>>> for i in xrange(ord("a"), ord("z")+1):
	if chr(i) in trans: print chr(i), trans[chr(i)]

	
a y
b n
c f
d i
e c
f w
g l
h b
i k
j u
k o
l m
m x
n s
o e
p v
r p
s d
t r
u j
v g
w t
x h
y a
>>> for i in xrange(ord("a"), ord("z")+1):
	if chr(i) in trans: print chr(i), trans[chr(i)]
	if chr(i) not in trans: print chr(i), "NOT"

	
a y
b n
c f
d i
e c
f w
g l
h b
i k
j u
k o
l m
m x
n s
o e
p v
q NOT
r p
s d
t r
u j
v g
w t
x h
y a
z NOT
>>> retrans = dict([(j, i) for (i, j) in trans.items()])
>>> retrans
{' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
>>> for i in xrange(ord("a"), ord("z")+1):
	if chr(i) in retrans: print chr(i), retrans[chr(i)]
	if chr(i) not in retrans: print chr(i), "NOT"

	
a y
b h
c e
d s
e o
f c
g v
h x
i d
j u
k i
l g
m l
n b
o k
p r
q NOT
r t
s n
t w
u j
v p
w f
x m
y a
z NOT
>>> trans
{' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h'}
>>> trans["q"] = "z"]
SyntaxError: invalid syntax
>>> trans["q"] = "z"
>>> trans["z"] = "q"
>>> gg = """30
ejp mysljylc kd kxveddknmc re jsicpdrysi
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
aej tysr dcmm rbksld yr xc neksl qeeex
"""
>>> for i in gg
KeyboardInterrupt
>>> ooo = ""
>>> for i in gg:
	ooo = ooo + trans[i]

	

Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    ooo = ooo + trans[i]
KeyError: '3'
>>> for i in xrang(10):
	trans[str(i)] = str(i)

	

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for i in xrang(10):
NameError: name 'xrang' is not defined
>>> for i in xrange(10):
	trans[str(i)] = str(i)

	
>>> for i in gg:
	ooo = ooo + trans[i]

	

Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    ooo = ooo + trans[i]
KeyError: '\n'
>>> trans["\n"] = "\n"
>>> for i in gg:
	ooo = ooo + trans[i]

	
>>> ooo
'3030\ncuv xadmuamf oi ohgciiosxf pc udkfvipadk\npnfvf avf prfdpy iob tawpcvoax gciiosoxopofi\nic op oi ceay ot ycu radp pc juip molf ug\nbcmme k yx rbc leelmc feic uyx rcdr iyry\nbet ypc aej\nyassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kccccccccc\na s w k f t m n o j e x h d c g q v i p u l y r b y z dcr o edcr hy aswi\ndfbp pohf rcdp ycu iodm ropn hf\nrny kc gvcmvahhfvi axrayi hob ug naxxcrffd adk wnvoiphai\ntcv pncif rnc igfae od a pcdmuf kc dcp igfae pc cpnfv gfcgxf\ndcscky udkfvipadki pnfh iodwf pnfy avf igfaeodm hyipfvofi od pnf igovop\nycu goiifk ctt pnf wnowefd xaky\naxx ycuv saif avf sfxcdm pc fvvcv pnf igccdy savk\ndcr pnap ycu edcr mccmxfvfif gxfaif kc dcp uif op pc nawe odpc cuv iyipfhi\nsy pnf gvoweodm ct hy pnuhsi ichfpnodm rowefk pnoi ray wchfi\ncn yfan axvomnp rfvf mcdda inaef op ug ropn pnf gavpy sfav pcdomnp\nop rai pnf sfip ct pohfi op rai pnf sxuvip ct pohfi\nrncccccccccccccccccccaaaaaaaaa o edcr w gxui gxui\nncr avf ycu ncxkodm ug sfwauif oh a gcpapc\ncuv wckf jah oi xoef pnf gypnamcvfad pnfcvfh\npnfvf oi dc adirfv\ngdfuhcdcuxpvahowvciwcgowioxowclcxwadcwcdocioi\ntvofdki kcdp xfp tvofdki xfp iwofdpotow gvcmvfii mc scode\nod a rcvxk ct kovfrcxlfi adk xocdi ichfpohfi pnf vavfip wvfapuvf oi a tvofdk\no nalf sfipfk tvuop igoef adk hccd dcr o inaxx sfip ycu pnf muy\npvadixapodm pfbp oi dcp mcvci ipvfdmpn\nipvfdmpn oi mcvci ipvfdmpn\nmvffpodmi wnffif gcgiowxf pnf duhsfv ycu nalf koaxfk oi wuvvfdpxy cup ct gcvewncgi\nkv zaoui kv zaoui kv zaoui kv zaoui ccccccccccccn kv zaoui\nycu radp ifxx pnodmi ap hf scodm zccch\n'
>>> 
KeyboardInterrupt
>>> ggg

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    ggg
NameError: name 'ggg' is not defined
>>> gg = """30
ejp mysljylc kd kxveddknmc re jsicpdrysi
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
aej tysr dcmm rbksld yr xc neksl qeeex
"""
>>> 
>>> ooo
'3030\ncuv xadmuamf oi ohgciiosxf pc udkfvipadk\npnfvf avf prfdpy iob tawpcvoax gciiosoxopofi\nic op oi ceay ot ycu radp pc juip molf ug\nbcmme k yx rbc leelmc feic uyx rcdr iyry\nbet ypc aej\nyassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kccccccccc\na s w k f t m n o j e x h d c g q v i p u l y r b y z dcr o edcr hy aswi\ndfbp pohf rcdp ycu iodm ropn hf\nrny kc gvcmvahhfvi axrayi hob ug naxxcrffd adk wnvoiphai\ntcv pncif rnc igfae od a pcdmuf kc dcp igfae pc cpnfv gfcgxf\ndcscky udkfvipadki pnfh iodwf pnfy avf igfaeodm hyipfvofi od pnf igovop\nycu goiifk ctt pnf wnowefd xaky\naxx ycuv saif avf sfxcdm pc fvvcv pnf igccdy savk\ndcr pnap ycu edcr mccmxfvfif gxfaif kc dcp uif op pc nawe odpc cuv iyipfhi\nsy pnf gvoweodm ct hy pnuhsi ichfpnodm rowefk pnoi ray wchfi\ncn yfan axvomnp rfvf mcdda inaef op ug ropn pnf gavpy sfav pcdomnp\nop rai pnf sfip ct pohfi op rai pnf sxuvip ct pohfi\nrncccccccccccccccccccaaaaaaaaa o edcr w gxui gxui\nncr avf ycu ncxkodm ug sfwauif oh a gcpapc\ncuv wckf jah oi xoef pnf gypnamcvfad pnfcvfh\npnfvf oi dc adirfv\ngdfuhcdcuxpvahowvciwcgowioxowclcxwadcwcdocioi\ntvofdki kcdp xfp tvofdki xfp iwofdpotow gvcmvfii mc scode\nod a rcvxk ct kovfrcxlfi adk xocdi ichfpohfi pnf vavfip wvfapuvf oi a tvofdk\no nalf sfipfk tvuop igoef adk hccd dcr o inaxx sfip ycu pnf muy\npvadixapodm pfbp oi dcp mcvci ipvfdmpn\nipvfdmpn oi mcvci ipvfdmpn\nmvffpodmi wnffif gcgiowxf pnf duhsfv ycu nalf koaxfk oi wuvvfdpxy cup ct gcvewncgi\nkv zaoui kv zaoui kv zaoui kv zaoui ccccccccccccn kv zaoui\nycu radp ifxx pnodmi ap hf scodm zccch\n'
>>> print ooo
3030
cuv xadmuamf oi ohgciiosxf pc udkfvipadk
pnfvf avf prfdpy iob tawpcvoax gciiosoxopofi
ic op oi ceay ot ycu radp pc juip molf ug
bcmme k yx rbc leelmc feic uyx rcdr iyry
bet ypc aej
yassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kassa yassa kccccccccc
a s w k f t m n o j e x h d c g q v i p u l y r b y z dcr o edcr hy aswi
dfbp pohf rcdp ycu iodm ropn hf
rny kc gvcmvahhfvi axrayi hob ug naxxcrffd adk wnvoiphai
tcv pncif rnc igfae od a pcdmuf kc dcp igfae pc cpnfv gfcgxf
dcscky udkfvipadki pnfh iodwf pnfy avf igfaeodm hyipfvofi od pnf igovop
ycu goiifk ctt pnf wnowefd xaky
axx ycuv saif avf sfxcdm pc fvvcv pnf igccdy savk
dcr pnap ycu edcr mccmxfvfif gxfaif kc dcp uif op pc nawe odpc cuv iyipfhi
sy pnf gvoweodm ct hy pnuhsi ichfpnodm rowefk pnoi ray wchfi
cn yfan axvomnp rfvf mcdda inaef op ug ropn pnf gavpy sfav pcdomnp
op rai pnf sfip ct pohfi op rai pnf sxuvip ct pohfi
rncccccccccccccccccccaaaaaaaaa o edcr w gxui gxui
ncr avf ycu ncxkodm ug sfwauif oh a gcpapc
cuv wckf jah oi xoef pnf gypnamcvfad pnfcvfh
pnfvf oi dc adirfv
gdfuhcdcuxpvahowvciwcgowioxowclcxwadcwcdocioi
tvofdki kcdp xfp tvofdki xfp iwofdpotow gvcmvfii mc scode
od a rcvxk ct kovfrcxlfi adk xocdi ichfpohfi pnf vavfip wvfapuvf oi a tvofdk
o nalf sfipfk tvuop igoef adk hccd dcr o inaxx sfip ycu pnf muy
pvadixapodm pfbp oi dcp mcvci ipvfdmpn
ipvfdmpn oi mcvci ipvfdmpn
mvffpodmi wnffif gcgiowxf pnf duhsfv ycu nalf koaxfk oi wuvvfdpxy cup ct gcvewncgi
kv zaoui kv zaoui kv zaoui kv zaoui ccccccccccccn kv zaoui
ycu radp ifxx pnodmi ap hf scodm zccch

>>> for i in gg:
	ooo = ooo + trans[i]
KeyboardInterrupt
>>> ooo = ""
>>> for i in gg:
	ooo = ooo + retrans[i]

	

Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    ooo = ooo + retrans[i]
KeyError: '3'
>>> for i in xrange(10):
	retrans[str(i)] = str(i)

	
>>> retrans["\n"] = "\n"
>>> ooo = ""
>>> for i in gg:
	ooo = ooo + retrans[i]

	

Traceback (most recent call last):
  File "<pyshell#69>", line 2, in <module>
    ooo = ooo + retrans[i]
KeyError: 'z'
>>> retrans["q"] = "z"]
SyntaxError: invalid syntax
>>> retrans["q"] = "z"
>>> retrans["z"] = "q"
>>> ooo = ""
>>> for i in gg:
	ooo = ooo + retrans[i]

	
>>> ooo
'30\nour language is impossible to understand\nthere are twenty six factorial possibilities\nso it is okay if you want to just give up\nxoggk d yl wxo vkkvgo ekso uyl wonw sywy\nxkf yto akj\nyabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dooooooooo\na b c d e f g h i j k l m n o p q r s t u v y w x y z now i know my abcs\nnext time wont you sing with me\nwhy do programmers always mix up halloween and christmas\nfor those who speak in a tongue do not speak to other people\nnobody understands them since they are speaking mysteries in the spirit\nyou pissed off the chicken lady\nall your base are belong to error the spoony bard\nnow that you know googlerese please do not use it to hack into our systems\nby the pricking of my thumbs something wicked this way comes\noh yeah alright were gonna shake it up with the party bear tonight\nit was the best of times it was the blurst of times\nwhoooooooooooooooooooaaaaaaaaa i know c plus plus\nhow are you holding up because im a potato\nour code jam is like the pythagorean theorem\nthere is no answer\npneumonoultramicroscopicsilicovolcanoconiosis\nfriends dont let friends let scientific progress go boink\nin a world of direwolves and lions sometimes the rarest creature is a friend\ni have bested fruit spike and moon now i shall best you the guy\ntranslating text is not goros strength\nstrength is goros strength\ngreetings cheese popsicle the number you have dialed is currently out of porkchops\ndr zaius dr zaius dr zaius dr zaius ooooooooooooh dr zaius\nyou want sell things at me boing zooom\n'
>>> print ooo
30
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
xoggk d yl wxo vkkvgo ekso uyl wonw sywy
xkf yto akj
yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dooooooooo
a b c d e f g h i j k l m n o p q r s t u v y w x y z now i know my abcs
next time wont you sing with me
why do programmers always mix up halloween and christmas
for those who speak in a tongue do not speak to other people
nobody understands them since they are speaking mysteries in the spirit
you pissed off the chicken lady
all your base are belong to error the spoony bard
now that you know googlerese please do not use it to hack into our systems
by the pricking of my thumbs something wicked this way comes
oh yeah alright were gonna shake it up with the party bear tonight
it was the best of times it was the blurst of times
whoooooooooooooooooooaaaaaaaaa i know c plus plus
how are you holding up because im a potato
our code jam is like the pythagorean theorem
there is no answer
pneumonoultramicroscopicsilicovolcanoconiosis
friends dont let friends let scientific progress go boink
in a world of direwolves and lions sometimes the rarest creature is a friend
i have bested fruit spike and moon now i shall best you the guy
translating text is not goros strength
strength is goros strength
greetings cheese popsicle the number you have dialed is currently out of porkchops
dr zaius dr zaius dr zaius dr zaius ooooooooooooh dr zaius
you want sell things at me boing zooom

>>> for (i, l) in enumerate(ooo.splitlines()):
	print "Case %d#: %s" % (i, l)

	
Case 0#: 30
Case 1#: our language is impossible to understand
Case 2#: there are twenty six factorial possibilities
Case 3#: so it is okay if you want to just give up
Case 4#: xoggk d yl wxo vkkvgo ekso uyl wonw sywy
Case 5#: xkf yto akj
Case 6#: yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dooooooooo
Case 7#: a b c d e f g h i j k l m n o p q r s t u v y w x y z now i know my abcs
Case 8#: next time wont you sing with me
Case 9#: why do programmers always mix up halloween and christmas
Case 10#: for those who speak in a tongue do not speak to other people
Case 11#: nobody understands them since they are speaking mysteries in the spirit
Case 12#: you pissed off the chicken lady
Case 13#: all your base are belong to error the spoony bard
Case 14#: now that you know googlerese please do not use it to hack into our systems
Case 15#: by the pricking of my thumbs something wicked this way comes
Case 16#: oh yeah alright were gonna shake it up with the party bear tonight
Case 17#: it was the best of times it was the blurst of times
Case 18#: whoooooooooooooooooooaaaaaaaaa i know c plus plus
Case 19#: how are you holding up because im a potato
Case 20#: our code jam is like the pythagorean theorem
Case 21#: there is no answer
Case 22#: pneumonoultramicroscopicsilicovolcanoconiosis
Case 23#: friends dont let friends let scientific progress go boink
Case 24#: in a world of direwolves and lions sometimes the rarest creature is a friend
Case 25#: i have bested fruit spike and moon now i shall best you the guy
Case 26#: translating text is not goros strength
Case 27#: strength is goros strength
Case 28#: greetings cheese popsicle the number you have dialed is currently out of porkchops
Case 29#: dr zaius dr zaius dr zaius dr zaius ooooooooooooh dr zaius
Case 30#: you want sell things at me boing zooom
>>> gg = """30
ejp mysljylc kd kxveddknmc re jsicpdrysi
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
aej tysr dcmm rbksld yr xc neksl qeeex
"""
KeyboardInterrupt
>>> gg = """30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
ys cac wep ys cac ysi y vklces wep y vklces
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
cyfb ew jd byd bkd ets dvcfkym lkwr ysi aej oset rbkd tyd xcysr re nc rpjc
ysi kw aej iesr jsicpcdrkxyrc xc k tesr jsicpcdrkxyrc aej
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
bet ypc aej bemiksl jv ncfyjdc kx y veryre
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
"""
>>> ooo = ""
>>> for i in gg:
	ooo = ooo + retrans[i]

	
>>> print ooo
30
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
xoggk d yl wxo vkkvgo ekso uyl wonw sywy
xkf yto akj
yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dooooooooo
a b c d e f g h i j k l m n o p q r s t u v y w x y z now i know my abcs
next time wont you sing with me
all your base are belong to error the spoony bard
friends dont let friends let scientific progress go boink
for those who speak in a tongue do not speak to other people
nobody understands them since they are speaking mysteries in the spirit
im commander shepard and this is my favorite problem on the google code jam
an eye for an eye and a pigeon for a pigeon
buff tryndamere and amumu
you know you want to
now that you know googlerese please do not use it to hack into our systems
oh hai im in ur computer eating your cheezburgers and googleresing your textz
i have bested fruit spike and moon now i shall best you the guy
each of us has his own special gift and you know this was meant to be true
and if you dont underestimate me i wont underestimate you
right i forgot here in the states you call it a sausage in the mouth
by the pricking of my thumbs something wicked this way comes
now is the summer of our lack of discontent
you better cut the pizza in four pieces because im not hungry enough to eat six
how are you holding up because im a potato
this here is gunpowder activated twenty seven caliber full auto no kickback nailthrowing mayhem
pneumonoultramicroscopicsilicovolcanoconiosis
in a world of direwolves and lions sometimes the rarest creature is a friend
greetings cheese popsicle the number you have dialed is currently out of porkchops

>>> for i in gg:
	ooo = ooo + retrans[i]
KeyboardInterrupt
>>> for (i, l) in enumerate(ooo.splitlines()):
	print "Case %d#: %s" % (i, l)

	
Case 0#: 30
Case 1#: our language is impossible to understand
Case 2#: there are twenty six factorial possibilities
Case 3#: so it is okay if you want to just give up
Case 4#: xoggk d yl wxo vkkvgo ekso uyl wonw sywy
Case 5#: xkf yto akj
Case 6#: yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dooooooooo
Case 7#: a b c d e f g h i j k l m n o p q r s t u v y w x y z now i know my abcs
Case 8#: next time wont you sing with me
Case 9#: all your base are belong to error the spoony bard
Case 10#: friends dont let friends let scientific progress go boink
Case 11#: for those who speak in a tongue do not speak to other people
Case 12#: nobody understands them since they are speaking mysteries in the spirit
Case 13#: im commander shepard and this is my favorite problem on the google code jam
Case 14#: an eye for an eye and a pigeon for a pigeon
Case 15#: buff tryndamere and amumu
Case 16#: you know you want to
Case 17#: now that you know googlerese please do not use it to hack into our systems
Case 18#: oh hai im in ur computer eating your cheezburgers and googleresing your textz
Case 19#: i have bested fruit spike and moon now i shall best you the guy
Case 20#: each of us has his own special gift and you know this was meant to be true
Case 21#: and if you dont underestimate me i wont underestimate you
Case 22#: right i forgot here in the states you call it a sausage in the mouth
Case 23#: by the pricking of my thumbs something wicked this way comes
Case 24#: now is the summer of our lack of discontent
Case 25#: you better cut the pizza in four pieces because im not hungry enough to eat six
Case 26#: how are you holding up because im a potato
Case 27#: this here is gunpowder activated twenty seven caliber full auto no kickback nailthrowing mayhem
Case 28#: pneumonoultramicroscopicsilicovolcanoconiosis
Case 29#: in a world of direwolves and lions sometimes the rarest creature is a friend
Case 30#: greetings cheese popsicle the number you have dialed is currently out of porkchops
>>> 
KeyboardInterrupt
>>> for (i, l) in enumerate(ooo.splitlines()):
	print "Case #%d: %s" % (i, l)

	
Case #0: 30
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
Case #4: xoggk d yl wxo vkkvgo ekso uyl wonw sywy
Case #5: xkf yto akj
Case #6: yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dabba yabba dooooooooo
Case #7: a b c d e f g h i j k l m n o p q r s t u v y w x y z now i know my abcs
Case #8: next time wont you sing with me
Case #9: all your base are belong to error the spoony bard
Case #10: friends dont let friends let scientific progress go boink
Case #11: for those who speak in a tongue do not speak to other people
Case #12: nobody understands them since they are speaking mysteries in the spirit
Case #13: im commander shepard and this is my favorite problem on the google code jam
Case #14: an eye for an eye and a pigeon for a pigeon
Case #15: buff tryndamere and amumu
Case #16: you know you want to
Case #17: now that you know googlerese please do not use it to hack into our systems
Case #18: oh hai im in ur computer eating your cheezburgers and googleresing your textz
Case #19: i have bested fruit spike and moon now i shall best you the guy
Case #20: each of us has his own special gift and you know this was meant to be true
Case #21: and if you dont underestimate me i wont underestimate you
Case #22: right i forgot here in the states you call it a sausage in the mouth
Case #23: by the pricking of my thumbs something wicked this way comes
Case #24: now is the summer of our lack of discontent
Case #25: you better cut the pizza in four pieces because im not hungry enough to eat six
Case #26: how are you holding up because im a potato
Case #27: this here is gunpowder activated twenty seven caliber full auto no kickback nailthrowing mayhem
Case #28: pneumonoultramicroscopicsilicovolcanoconiosis
Case #29: in a world of direwolves and lions sometimes the rarest creature is a friend
Case #30: greetings cheese popsicle the number you have dialed is currently out of porkchops
>>> 
