import sys

Ag = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
Bg = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
Cg = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

Ae = "our language is impossible to understand"
Be = "there are twenty six factorial possibilities"
Ce = "so it is okay if you want to just give up"




let_dict = { 'e':'o', 'y':'a', 'q':'z' }


for (goog, eng) in [(Ag, Ae), (Bg, Be), (Cg, Ce)]:
    for i in range(0, len(goog)):
        let_dict[goog[i]] = eng[i]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = None
value = None

for i in range(0, len(alphabet)):
    ilet = alphabet[i]
    if ilet not in let_dict.keys():
        key = ilet
    if ilet not in let_dict.values():
        value = ilet

let_dict[key] = value


in_file = open(sys.argv[1])

num_samples = in_file.readline().strip()

num_samples = int(num_samples)

for i in range(0, num_samples):
    goog_lang = in_file.readline().strip()
    eng_lang = ''
    for j in range(0, len(goog_lang)):
        eng_lang += let_dict[goog_lang[j]]
    print 'Case #%s: %s' % (i+1, eng_lang)

