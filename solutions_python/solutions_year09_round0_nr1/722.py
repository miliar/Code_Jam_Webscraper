from sys import argv

def __main__():
    file = open(argv[1])
    dict = []
    i = 0
    c = 0
    for line in file:
        line = line.strip()
        if not len(line):
            continue
        if i == 0:
            toks = line.split()
            L = int(toks[0])
            D = int(toks[1])
            N = int(toks[2])
        elif i <= D:
            dict.append(line)
        else:
            c += 1
            print 'Case #' + str(c) + ':',
            possibles = []
            parent = False
            for e in line:
                if e == '(':
                    parent = True
                    l = []
                elif e == ')':
                    possibles += [l]
                    parent = False
                else:
                    if parent:
                        l.append(e)
                    else:
                        possibles += [[e]]
                    


            #print possibles
            p = 0
            for word in dict:
                e = 0
                while e < L:
                    #print word, possibles, e
                    if word[e] not in possibles[e]:
                        break
                    e += 1
                if e==L:
                    p+=1
            print p
        i += 1
    file.close()

__main__()