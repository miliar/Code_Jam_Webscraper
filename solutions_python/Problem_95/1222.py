
infile = open("A-small-attempt1.in")
outfile = open("A-small-attempt1.out", "w")

#infile = open("a.input.txt")
#outfile = open("a.output.txt", "w")

mapping = {
    'y':'a',
    'e':'o',
    'q':'z',
    'j':'u',
    'p':'r',
    'm':'l',
    's':'n',
    'l':'g',
    'c':'e',
    'k':'i',
    'd':'s',
    'x':'m',
    'v':'p',
    'd':'s',
    'n':'b',
    'r':'t',
    'i':'d',
    't':'w',
    'a':'y',
    'h':'x',
    'w':'f',
    'f':'c',
    'o':'k',
    'b':'h',
    'g':'v',
    'u':'j',
    'z':'q'}

n = int(infile.readline())

for casenum in range(0, n):

    print ("Case %d" % casenum)
    line = infile.readline().strip()

    out = []
    for c in line:
        if mapping.has_key(c):
            out.append(mapping[c])
        else:
            out.append(c)
    out = "".join(out)

    outfile.write("Case #%d: %s\n" % (casenum+1, out))
    
infile.close()
outfile.close()

print("ok")

