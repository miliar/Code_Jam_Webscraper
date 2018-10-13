a =["ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
b = ["our language is impossible to understand",
     "there are twenty six factorial possibilities",
     "so it is okay if you want to just give up"]

dict = {}
for i in range(0, 3):
    for j in range(0, len(a[i])):
        dict[a[i][j]] = b[i][j]

dict['q'] = 'z'
dict['z'] = 'q'
    
"""print len(dict)
print dict
c = 'a'
while c <= 'z':
    if c not in dict:
        print c
    c = chr(ord(c) + 1)

c = 'a'
while c <= 'z':
    if c not in dict.keys():
        print c
    c = chr(ord(c) + 1)"""


with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as ou:
        a = inp.readlines()
        n = int(a[0].strip())
        i = 0
        i -= 1
        for x in a[1:]:
            y = ""
            i += 1
            x = x.strip()
            for c in x:
                y += dict[c]
            print >>ou, "Case #%d:" % (i+1), y
