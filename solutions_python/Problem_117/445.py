import sys

name = sys.argv[1]

with open(name) as f:
    lines = list()
    for index, line in enumerate(f.readlines()[1:]):
        lines.append(line[:-1] if line[-1] == '\n' else line)
        
    # print lines
    index = 0
    counter = 0
    while True:
        if index == len(lines):
            break
        n, m = [int(a) for a in lines[index].split()]
        
        lignes, colonnes = list(), list()
        for i in range(n):
            index += 1
            l = [int(a) for a in lines[index].split()]
            lignes.append((max(l), l))
        for i in range(m):
            c = list()
            for l in lignes:
                c.append(l[1][i])
            colonnes.append((max(c), c))
                
        # print lignes
        # print colonnes
        
        def check():
            for ml, l in lignes:
                for i, (mc, c) in enumerate(colonnes):
                    if l[i] != ml and l[i] != mc:
                        return "NO"
            return "YES"
        out = check()
        index += 1
        counter += 1
        print "Case #%d: %s" % (counter, out)
        out = str()
        ####################################
