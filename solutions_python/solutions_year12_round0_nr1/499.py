input_file = raw_input("input_file:\n")
output_file = "output.txt"

alphabet = "abcdefghijklmnopqrstuvwxyz"

cyphers = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

plains = ["our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"]

googlerese = {}
for letter in alphabet:
    googlerese[letter] = 0
googlerese[' '] = ' '
for cypher, plain in zip(cyphers, plains):
    for code, decode in zip(cypher, plain):
        googlerese[code] = decode
#print googlerese
#print set(alphabet) - set([googlerese[letter] for letter in alphabet])

op = raw_input("Input option:\n")
if op == '1':
    googlerese['q'] = 'q'
    googlerese['z'] = 'z'
elif op == '0':
    googlerese['q'] = 'z'
    googlerese['z'] = 'q'
else:
    raise "Bad input, Michael"

inp = open(input_file, 'r')
out = open(output_file, 'w')
n = int(inp.readline())
for i in range(1, n + 1):
    line = inp.readline()
    out.write("Case #" + str(i) + ": ")
    for char in line:
        if char == ' ':
            out.write(' ')
        elif 'a' <= char and char <= 'z':
            out.write(googlerese[char])
    out.write("\n")

inp.close()
out.close()
print "Done!"

