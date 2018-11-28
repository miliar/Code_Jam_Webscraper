mapping = list("-" * 26)
mapping[0] = "y"
mapping[ord("o") - ord("a")] = "e"
mapping[25] = "q"
mapping[16] = "z"
    
inp = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
outp = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

for i in range(len(inp)):
    if inp[i] == " ": continue
    mapping[ord(inp[i]) - ord('a')] = outp[i]

mapping = ''.join(mapping)

i = -1
for line in open("A-small-attempt0.in"):
    i += 1
    if i == 0:
        continue
    s = list(line.strip())
    for j in range(len(s)):
        if s[j] == " ": continue
        idx = ord(s[j]) - ord('a')
        s[j] = mapping[idx]
    s = ''.join(s)
    print "Case #" + str(i) + ": " + s
