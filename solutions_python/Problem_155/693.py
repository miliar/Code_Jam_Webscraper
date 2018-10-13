fin = open("input.in", "r")
fout = open("out.txt", 'w')
file = fin.read().split('\n')
file.pop(0)
for count, line in enumerate(file):
    audience = [int(x) for x in list(line.split()[1])]
    clap = audience[0]
    i = 1
    extra = 0
    for i in range(1, len(audience)):
        if clap < i:
            extra += i - clap
            clap += i - clap
        clap += audience[i]
    
    fout.write("Case #{0}: {1}\n".format(count + 1, extra))
fout.close()
fin.close()
