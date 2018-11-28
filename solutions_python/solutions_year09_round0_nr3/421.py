cases="""cewoacoaedcqoeoe a
weulcome   to cccoddde   jaaam
wwelcoome t o  code  jam
xwelcome tto colcde  jmam
welcome to code jam
weelcommee  oto coede jam
mw jeejee aoceog
nl    mljc  mooalq
wwwwwwwelcome to code jjjam
zwexescweoodl e  k
cwelcomee teo coede  jamn
my vdmsoddwtm wh
welcome to code jam
ywespxlcoxme tuoh ycsbodie jam
pj dfojcctc ooamu
uaacse ewcmt dm
wcelccoommeme t o cooode jjam
wewellcco mee oto code jaam
wwelcome to code  jam
welcome to code jam
fm  bjjecoeeoeooay
pedlwofo edmoo eot
wweellccoommee to code qps jam
h  t  gdoemecew
wweloceomoe to code jam
welcoome to code jam
wwwelllcome tto code jjjjjamm
eoe emowjmeood l mmawmlh
wellcomee to ccodee jaam
welcome to code jamjamjamjam
wtelolcom e toe ocojmdee jamx
welcoome to ccodde jam
wwelcome tto coocde jjaamm
emctwcleloeoojcol
w
pwelcoyme   ttto coddukdeg jam
welclcome to ccode jam
wweclcomee  oto cdodde jam
cemmjelmelcmmaels
bdemej msomceme
wellcooeme to codde jam
welco  cme two mecode de jam
welcome to code jam
welcome to code jam
wellcocmome totooc cdodje jam
zejjkwt  koooaeet
welllcooomeee ttto coddde jam
wwelccomemte to ccoddee jaamm
oow o owet eg mel
not really a welcome message
wellcome  t o coede jjam
fcwweloo zowoor
wwellcmome to ocode jam
welcome to ccdode jam
welcomee to code jam
wellcoommee  to c oode jajmm
welcome to  code  jam
oml ewtcommrtjmlq
welccome tto coded jjam
jceaatkece mcci
welcome to occode jam
welcellcome too codee jaemm
m cacl tleoo lczo  o dommdaj
jeeowltjtxeeecejmn
n  ecj etwmtaaa
weelcome  otoo code jaam
wewelccomme  tto coded  jjamm
z
baap cooomewctsto
welcome to code jaam
idom  ltm dj ok
admaljmeeome ce
wwellcomee  ttoo coode  jjaam
welcome to codejam
xe wec cdcam jtdmi
elcomew elcome to code jam
welccomee ttoo code  jjam
q welcome to code jam p
wel lcoomee to codoed  e jjam
weleclome to  ccode  jtam
welcome to code jam
weelccommee tto c ocde ejammm
weelccom eo to cdode jam
welccome to ccoede jam
wellcome tto code jam
wwhelcoomeme tof coode jamam
welcome t o cocdoee jjamm
wwelcocwomee t o code  jamjm
welcormoea tlo co dae emjaem z
weelccoome  t o coode  jamm
welcomme to code jjam
you are welcomed to code jam
wweellcome to cocdee j aam
welcoooooooooome to code jam
ulcca kaeawtwef
wellcome to codde jam
awemremojeeecljoedajoor
welcomoe to coded jjaam
welcome to  coodde jamm
xto  lweetodmmmj"""


small="welcome to code jam"
#big="wweellccoommee to code qps jam"


class Memoize:
    def __init__(self,function):
        self._cache = {}
        self._callable = function
            
    def __call__(self, *args, **kwds):
        cache = self._cache
        key = self._getKey(*args,**kwds)
        try: return cache[key]
        except KeyError:
            cachedValue = cache[key] = self._callable(*args,**kwds)
            return cachedValue
    def clear(self):
		self.cache={}
    def _getKey(self,*args,**kwds):
        return kwds and (args, ImmutableDict(kwds)) or args    
	

import sys
sys.setrecursionlimit(100000)

@Memoize
def f(big, s=0, b=0):
	"calculate how many times target[i:] is in string[j:]"
	if s==19:
		return 1
	if b==len(big):
		return 0
	if small[s]==big[b]:
		x=f(big, s+1, b+1)
	else:
		x=0
	return (x + f(big, s, b+1))

t=1
for case in cases.split("\n"):
	print "Case #%d: %04d"% (t, f(case))
	#print dir(f)
	t+=1