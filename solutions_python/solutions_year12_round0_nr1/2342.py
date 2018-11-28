alphabet = "abcdefghijklmnopqrstuvwxyz"
map = "yhesocvxduiglbkrztnwjpfmaq"
def translate(s):
    for i in range(0, len(s)):
        if s[i] in alphabet:
            index = alphabet.index(s[i])
            s[i] = map[index]
    return "".join(s)
f = open('small.in', 'r')
outputf = open('small.out', 'w')
i =  int(f.readline())
for m in range(0, i):
    s = list(f.readline())
    outputf.write("Case #" + str(m + 1) + ': ' + translate(s))
