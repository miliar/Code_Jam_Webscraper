fin = open("input", "r")
fout = open("output", "r+")

in1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
in2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
in3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

out1 = "our language is impossible to understand"
out2 = "there are twenty six factorial possibilities"
out3 = "so it is okay if you want to just give up"

trans = {}
trans['y'] = 'a'
trans['e'] = 'o'
trans['q'] = 'z'
trans['z'] = 'q'

for i in range(len(in1)):
    trans[in1[i]] = out1[i]

for i in range(len(in2)):
    trans[in2[i]] = out2[i]

for i in range(len(in3)):
    trans[in3[i]] = out3[i]

n = int(fin.readline())
#print(n)

for i in range(n):
    line = str(fin.readline())
    if line[-1:] == "\n":
        line = line[0:-1]
    output = "Case #"+str(i+1)+": "
    for char in line:
        output += trans[char]
    fout.write(output + "\n")


fin.close()
fout.close()
