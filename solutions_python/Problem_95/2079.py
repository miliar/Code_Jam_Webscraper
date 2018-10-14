alpha = "qwertyuioplkjhgfdsazxcvbnm"

mapping = {}
mapping["a"]="y"
mapping["o"]="e"
mapping["z"]="q"
mapping["q"]="z"

in1 ="ejp mysljylc kd kxveddknmc re jsicpdrysi"
out1="our language is impossible to understand"

in2 ="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
out2="there are twenty six factorial possibilities"

in3 ="de kr kd eoya kw aej tysr re ujdr lkgc jv"
out3="so it is okay if you want to just give up"

def translate(s):
    out =""
    for c in s:
        out+=mapping[c]
    return out

def buildMap(inS, outS):
    if len(inS) != len(outS):
        return -1
    i=0
    while i < len(inS):
        mapping[inS[i]]=outS[i]
        i+=1

def printTrans():
    for c in alpha:
        if c in mapping :
            print c,":",mapping[c]
        else:
            print c,":NAN"
    tmp=[]
    for v in mapping:
        tmp.append(mapping[v])
    for c in alpha:
        if not c in tmp:
            print c+" not Found"
        
        

def load():
    buildMap(in1,out1)
    buildMap(in2,out2)
    buildMap(in3,out3)

load()


inAr = [
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
"hello i am the google code jam test data",
"how are you",
"aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee",
"y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd",
"schr rkxc tesr aej dksl tkrb xc",
"mcr mkvd ie tbyr bysid ie",
"aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh",
"rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx",
"ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd",
"na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd",
"kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd",
"ejp feic uyx kd mkoc rbc varbylepcys rbcepcx",
"rbcpc kd se ysdtcp",
"tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd",
"ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi",
"aej tysr dcmm rbksld yr xc neksl qeeex",
"k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja",
"eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr",
"dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks",
"rpysdmyrksl rchr kd ser leped drpcslrb",
"drpcslrb kd leped drpcslrb",
"xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej",
"ys cac wep ys cac ysi y vklces wep y vklces",
"wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc",
"seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr",
"set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr",
"eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq"]
cnt=1
for test in inAr:
    print "Case #"+str(cnt)+": "+translate(test)
    cnt+=1
