normal = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq"
encrypted = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz"
dictionary = "abcdefghijklmnopqrstuvwxyz "
dictcrypt =  "ynficwlbkuomxsevzpdrjgthaq "
buff = ""
f = open("testcase", "r+").readlines()
print "cantidad de lineas %s" % f[0]

def getClear(text):
    texto = ""
    for i in text:
        number = dictcrypt.find(i)
        texto += dictionary[number]
    return texto

for linea in range(1, len(f)):
    texto = getClear(f[linea])
    buff += "Case #%s: %s\n"%(linea, texto)

fi = file("testcase.o", "w+")
fi.write(buff)
fi.close()
