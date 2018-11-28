mapping = {' ': ' ', 'B': 'H', 'D': 'S', 'F': 'C', 'H': 'X', 'J': 'U', 'L': 'G', 'N': 'B',
 'P': 'R', 'R': 'T', 'T': 'W', 'V': 'P', 'X': 'M', 'Z': 'Q', 'b': 'h', 'd': 's',
 'f': 'c', 'h': 'x', 'j': 'u', 'l': 'g', 'n': 'b', 'p': 'r', 'r': 't', 't': 'w',
 'v': 'p', 'x': 'm', 'z': 'q', 'A': 'Y', 'C': 'E', 'E': 'O', 'G': 'V', 'I': 'D',
 'K': 'I', 'M': 'L', 'O': 'K', 'Q': 'Z', 'S': 'N', 'U': 'J', 'W': 'F', 'Y': 'A',
 'a': 'y', 'c': 'e', 'e': 'o', 'g': 'v', 'i': 'd', 'k': 'i', 'm': 'l', 'o': 'k',
 'q': 'z', 's': 'n', 'u': 'j', 'w': 'f', 'y': 'a'}

input = '''30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
ip qykjd ip qykjd ip qykjd ip qykjd eeeeeeeeeeeeb ip qykjd
bet ypc aej bemiksl jv ncfyjdc kx y veryre
set kd rbc djxxcp ew ejp myfo ew ikdfesrcsr
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
ys cac wep ys cac ysi y vklces wep y vklces
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
dtkwr yd rbc tksi zjkcr yd rbc wepcdr drcyia yd rbc xejsryks
ejp feic uyx kd mkoc rbc varbylepcys rbcepcx
rbcpc kd se ysdtcp
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd
aej vkddci eww rbc fbkfocs myia
w ew rte czjymd w ew esc czjymd esc
wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
'''.split("\n")

n = int(input[0])

inputs = input[1:]

for i, line in enumerate(inputs):
  print "Case #%s: %s"%(i+1, ''.join(map(lambda x: mapping[x], list(line))))