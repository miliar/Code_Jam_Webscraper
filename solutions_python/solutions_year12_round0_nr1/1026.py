input = open("sit.in" , "r")
output = open("sit.out" , "w")
cases = int(input.readline())

key = list("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z")
value = list("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q")

trans = {}

for i in range(len(value)):
    trans[key[i]] = value[i]

for j in range(1, cases + 1):
    line = list(str(input.readline()).strip())
    lated = []
    for k in line:
        lated.append(trans[k])
    lated = str("".join(lated))
    print "Case #" + str(j) + ": " + lated
    output.write("Case #" + str(j) + ": " + lated + "\n")
input.close()
output.close()
