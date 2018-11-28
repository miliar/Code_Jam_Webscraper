f = open('A-small-attempt1.in', 'r')
o = open('A-small-attempt1.out', 'w')

translation = {}
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for a in alpha:
    translation[a] = 'a'

en = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
de = "our language is impossible to understand"
for x in range(0,len(en)):
    translation[en[x]] = de[x]

en = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
de = "there are twenty six factorial possibilities"
for x in range(0,len(en)):
    translation[en[x]] = de[x]

en = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
de = "so it is okay if you want to just give up"
for x in range(0,len(en)):
    translation[en[x]] = de[x]
    
translation['z'] = 'q'
translation['q'] = 'z'

def translate(encrypted):
    encrypted = encrypted[0:len(encrypted) - 1]
    decrypted = ""
    for x in range(0, len(encrypted)):
        decrypted = decrypted + translation[encrypted[x]]
    return decrypted

num = int(f.readline())
for x in range(0,num):
    encrypted = f.readline()
    decrypted = translate(encrypted)
    o.write("Case #" + str(x+1) + ": " + decrypted + "\n")

f.close()
o.close()
