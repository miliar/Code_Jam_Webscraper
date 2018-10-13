mapped_letters = {}
mapped_letters['a'] = 'y'
mapped_letters['o'] = 'e'
mapped_letters['z'] = 'q'
mapped_letters['e'] = 'j'
mapped_letters['q'] = 'z'
inp = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

out = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

for i in range(len(inp)):
    a = inp[i]
    b = out[i]
    for x in range(len(a)):
        mapped_letters[a[x]] = b[x]

N = int(raw_input())
for i in range(N):
    line = raw_input()
    out = ""
    for x in line:
        out += mapped_letters[x]
    print "Case #" + str(i+1) + ": " + out
