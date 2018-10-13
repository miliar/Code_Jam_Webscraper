dictIn = open("dict.in", "r")
dictOut = open("dict.out", "r")
fi = open("input.txt", "r")
fo = open("output.txt", "w")

text = dictIn.readlines()
translate = dictOut.readlines()

m = {}
x = {}
m['z'] = 'q'
m['o'] = 'e'
x['e'] = 'o'
x['q'] = 'z'

for i in range(len(text)):
    for j in range(len(text[i])):
        m[text[i][j]] = translate[i][j]
        x[translate[i][j]] = text[i][j]

print (m)
n = int(fi.readline().strip())
for tests in range(n):
    inp = list(fi.readline())
    for i in range(len(inp)):
        if inp[i] in m:
            inp[i] = m[inp[i]]
        else:
            inp[i] = x[inp[i]]
    fo.write(("Case #%d: " % (tests + 1)) + "".join(inp))