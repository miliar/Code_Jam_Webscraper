mapping = {'a' : 'y',
           'b' : 'h',
           'c' : 'e',
           'd' : 's',
           'e' : 'o',
           'f' : 'c',
           'g' : 'v',
           'h' : 'x',
           'i' : 'd',
           'j' : 'u',
           'k' : 'i',
           'l' : 'g',
           'm' : 'l',
           'n' : 'b',
           'o' : 'k',
           'p' : 'r',
           'q' : 'z',
           'r' : 't',
           's' : 'n',
           't' : 'w',
           'u' : 'j',
           'v' : 'p',
           'w' : 'f',
           'x' : 'm',
           'y' : 'a',
           'z' : 'q',
           ' ' : ' ',
           '\n' : '\n'
}

inp = open("input.txt","r");
out = open("output.txt","w");
inp.readline()
for i,line in enumerate(inp.readlines()):
    txt = ""
    for c in line:
        txt = txt+mapping[c]
    out.write("Case #"+str(i+1)+": "+txt)
out.close()

