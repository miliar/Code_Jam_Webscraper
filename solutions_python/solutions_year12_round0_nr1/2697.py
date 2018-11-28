fp = open('A-small-attempt2.in', 'r')
data = fp.read()
fp.close()

count = data[1]
data = data[2:]

hash = {
    'a':'y',
    'b':'h',
    'c':'e',
    'd':'s',
    'e':'o',
    'f':'c',
    'g':'v',
    'h':'x',
    'i':'d',
    'j':'u',
    'k':'i',
    'l':'g',
    'm':'l',
    'n':'b',
    'o':'k',
    'p':'r',
    'q':'z',
    'r':'t',
    's':'n',
    't':'w',
    'u':'j',
    'v':'p',
    'w':'f',
    'x':'m',
    'y':'a',
    'z':'q'
}

fp = open("output", 'w')
count = 1
for i in data:
    if i == "\n":
        if count != 1:
            fp.write("\n")
        fp.write("Case #" + str(count)+ ": ")
        count += 1
        continue
    fp.write(hash.get(i, i))
fp.close()
