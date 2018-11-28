
def findall(string, sub, start=0):
    p = 0
    s = start
    l = []
    
    while p != -1:
        p = string.find(sub, s)
        
        if p != -1:
            s = p + 1
            l.append(p)
    
    return l

def mktree(tree):
    curr = tree.pop(0)
    alis = []
    hijo = []

    if tree:
        hijo = mktree(tree)

    for each in curr:
        if hijo:
            for ehij in hijo:
                fal = False
                sec = [each]
                for cehij in ehij:
                    if each < cehij:
                        sec.append(cehij)
                    else:
                        fal = True
                        break
                if not fal:
                    alis.append(sec)
        else:
            alis.append([each])

    return alis

def main():
    FILENAME = 'C-small-attempt2'
    WELCOME = 'welcome to code jam'
    
    output = open(FILENAME + '.out', 'w')
    lines = open(FILENAME + '.in', 'r').readlines()
    count = int(lines[0])
    lines = lines[1:]
    
    for i in range(count):
        line = lines[i].strip()
        lista = []
        pos = 0
        
        for n in range(len(WELCOME)):
            lista.append(findall(line, WELCOME[n], pos))
            pos = line.find(WELCOME[n], pos)
        
        tree = mktree(lista)
        number = 0
        
        for arbol in tree:
            if len(arbol) == len(WELCOME):
                number += 1
        
        output.write("Case #%d: %04d\n" % (i + 1, number))
    
    output.close()

if __name__ == '__main__':
    main()