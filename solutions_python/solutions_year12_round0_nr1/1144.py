class GCJ1:
    d = {}
    src='abcdefghijklmnopqrstuvwxyz'
    terminated = False
    def InitializeD(self):
        for r in self.src:
            self.d[r]=''
    def Test(self, lines):
        res=[]
        lns = lines.splitlines()
        maxitems = len(lns)
        for i in range(1,maxitems):
             res.append("Case #" + str(i) + ": " + self.Decode(lns[i]) + '\n')
        return "".join(res)
        
    def Learn(self,original,translated):
        owords = original.split()
        twords = translated.split()
        cur = 0
        cur2 = 0
        self.d[' '] = ' '
        for cur in range(len(owords)):
            oword = owords[cur]
            tword = twords[cur]
            for cur2 in range(len(oword)):
                self.d[oword[cur2]] = tword[cur2]
        if not self.terminated:
            self.TryTerminate()
        
    def TryTerminate(self):
        res = [r for r in self.d if self.d[r]=='']
        if(len(res)==1):
            rt = [self.d[r] for r in self.d if self.d[r]!='']
            for s in self.src:
                if not s in rt:
                    self.d[res[0]]=s
                    self.terminated = True
                    return
        
    def Decode(self,gstring):
        res = []
        for s in gstring:
            if s in self.d:
                res.append(self.d[s])
            else:
                res.append('[ND]')
        return "".join(res)

gc = GCJ1()
gc.InitializeD()
gc.Learn("q","z")
gc.Learn("e","o")
gc.Learn("y","a")

gc.Learn("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
gc.Learn("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities")
gc.Learn("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")






print(gc.Test("""30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
rbkd bcpc kd ljsveticp yfrkgyrci rtcsra dcgcs fymkncp wjmm yjre se okfonyfo sykmrbpetksl xyabcx
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
pklbr k wepler bcpc ks rbc dryrcd aej fymm kr y dyjdylc ks rbc xejrb
rbyso aej njr rbc pcym leelmcpcdc kd ks yserbcp fydrmc
mcr mkvd ie tbyr bysid ie
bet ypc aej bemiksl jv ncfyjdc kx y veryre
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
w ew rte czjymd w ew esc czjymd esc
wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte
"""))

