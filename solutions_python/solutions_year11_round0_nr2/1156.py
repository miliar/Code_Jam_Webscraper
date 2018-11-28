def magic(combo, clear, spell):
    if not len(spell):
        return []    
    clears = set([])
    last = spell[0]
    pointer = 1
    while len(spell) > pointer:
        c = spell[pointer]
        try:
            spell = spell[:pointer-1] + combo[c][last] + spell[pointer+1:]
            last = combo[c][last]
        except:
            clears.update(clear[last])
            if c in clears:
                spell = spell[pointer+1:]
                clears = set([])
                if not len(spell):
                    continue                
                last = spell[0]
                pointer = 1
            else:
                last = c
                pointer += 1
    return [i for i in spell]

f = open('input')
g = open('output.txt', 'w')
tests = int(f.readline())
for t in xrange(tests):
    combo = {}
    clear = {}
    for i in xrange(ord('A'), ord('Z')+1):
        combo[chr(i)] = {}
        clear[chr(i)] = set([])
    line = f.readline()[:-1].split(' ')
    C = int(line[0])
    D = int(line[C+1])
    N = int(line[C+D+2])
    for i in xrange(C):
        a,b,c = tuple([x for x in line[i+1]])
        combo[a][b] = c
        combo[b][a] = c
    for i in xrange(D):
        a,b = tuple([x for x in line[i+C+2]])
        clear[a].add(b)
        clear[b].add(a)
    out = 'Case #' + str(t+1) + ': '+ str(magic(combo, clear, line[C+D+3]))
    out = out.replace("'", "")    
    print out
    g.write(out+'\n')

f.close()
g.close()
