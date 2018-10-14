#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Dmytro Molkov on 2012-04-13.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os

inputs = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
rbkd kd de chfkrksl k bygc re le rbc nyrbpeex
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
bet ypc aej bemiksl jv ncfyjdc kx y veryre
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
xa syxc kd ijl k bygc ujdr xcr aej ysi k meeegc aej
rpysdmyrksl rchr kd ser leped drpcslrb
drpcslrb kd leped drpcslrb
kr tyd rbc ncdr ew rkxcd kr tyd rbc nmjpdr ew rkxcd
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
set rbyr aej oset leelmcpcdc vmcydc ie ser jdc kr re byfo ksre ejp dadrcxd
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
rbyso aej njr rbc pcym leelmcpcdc kd ks yserbcp fydrmc
mcr mkvd ie tbyr bysid ie
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
ymm aejp nydc ypc ncmesl re cppep rbc dveesa nypi
ys cac wep ys cac ysi y vklces wep y vklces
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
eb acyb ympklbr tcpc lessy dbyoc kr jv tkrb rbc vypra ncyp resklbr
vscjxesejmrpyxkfpedfevkfdkmkfegemfysefeskedkd
aej vkddci eww rbc fbkfocs myia"""
def main():
    str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    str2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    str3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
    
    str1_t = "our language is impossible to understand"
    str2_t = "there are twenty six factorial possibilities"
    str3_t = "so it is okay if you want to just give up"
    orig = [str1, str2, str3]
    trans = [str1_t, str2_t, str3_t]
    
    mapping = {'y': 'a', 'e':'o', 'q':'z', 'z':'q'}
    alphabet = set()
    
    for i in range(3):
        for j in range(len(orig[i])):
            mapping[orig[i][j]] = trans[i][j]
    al = mapping.values()
    al.sort()
    print al
    lines = inputs.split("\n")
    i = 0
    for line in lines:
        i+= 1
        print 'Case #' + str(i) + ": " + convert(line, mapping)

def convert(line, mapping):
    """docstring for convert"""
    result = ""
    for i in range(len(line)):
        result += mapping[line[i]]
    return result
if __name__ == '__main__':
    main()

