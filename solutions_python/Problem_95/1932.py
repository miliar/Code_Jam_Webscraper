T = int(input())

slownik = {'q': 'z', 'y': 'a', 'e': 'o', 'z': 'q'}

templates = [("ejp mysljylc kd kxveddknmc re jsicpdrysi",
              "our language is impossible to understand"),
             ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
              "there are twenty six factorial possibilities"),
             ("de kr kd eoya kw aej tysr re ujdr lkgc jv",
              "so it is okay if you want to just give up")]

for (coded, uncoded) in templates:
    for i in range(len(uncoded)):
        slownik[coded[i]]=uncoded[i]

for i in range(1,T+1):
    text = input()
    out = ""
    for c in text:
        out+=slownik[c]
    print("Case #{0}: {1}".format(i, out))
