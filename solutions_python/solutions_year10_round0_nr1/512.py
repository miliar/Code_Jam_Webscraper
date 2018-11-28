# -*- coding: utf-8 -*-

snaps = {1:2,
2:4,
3:8,
4:16,
5:32,
6:64,
7:128,
8:256,
9:512,
10:1024,
11:2048,
12:4096,
13:8192,
14:16384,
15:32768,
16:65536,
17:131072,
18:262144,
19:524288,
20:1048576,
21:2097152,
22:4194304,
23:8388608,
24:16777216,
25:33554432,
26:67108864,
27:134217728,
28:268435456,
29:536870912,
30:1073741824}

inp = open("A-large.in","r")
outp = open("output.out","w")

lines = inp.readline()
lines = lines.split()
lines = int(lines[0])

for i in range (0,lines):
    outp.write ("Case #" + str(i+1) + ": ")
    test = inp.readline()
    test = test.split ()
    test[0] = int (test[0])
    test[1] = int (test[1])

    if test[1] % snaps[test[0]] == snaps[test[0]]-1:
        outp.write("ON"+"\n")
    else:
        outp.write("OFF"+"\n")


inp.close()
outp.close()

