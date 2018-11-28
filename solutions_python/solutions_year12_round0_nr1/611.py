import sys
map = {
"y":"a",
"n":"b",
"f":"c",
"i":"d",
"c":"e",
"w":"f",
"l":"g",
"b":"h",
"k":"i",
"u":"j",
"o":"k",
"m":"l",
"x":"m",
"s":"n",
"e":"o",
"v":"p",
"z":"q",
"p":"r",
"d":"s",
"r":"t",
"j":"u",
"g":"v",
"t":"w",
"h":"x",
"a":"y",
"q":"z",
}

num = raw_input()

for i in range(int(num)):
    line = raw_input()
    out = ""
    out = out + "Case #" + str(i+1) + ": "
    for x in line:
        if x == ' ':
            out = out + x
        else:
            out = out + map[x]
    print out

