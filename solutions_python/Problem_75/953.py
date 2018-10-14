
with open('magicka.in', 'r') as fin:
    lines = fin.readlines()
    T = int(lines[0])

for t in range(T):
    bits = lines[t+1].split()
    C = int(bits[0])
    combos = {}
    for c in range(C):
        st = bits[1 + c]
        combos[(st[0], st[1])] = st[2]
        combos[(st[1], st[0])] = st[2]
    D = int(bits[1 + C])
    destructs = {}
    for d in range(D):
        st = bits[1 + C + 1 + d]
        if not destructs.has_key(st[0]):
            destructs[st[0]] = set()
        destructs[st[0]].add(st[1])
        if not destructs.has_key(st[1]):
            destructs[st[1]] = set()
        destructs[st[1]].add(st[0])
    N = int(bits[1 + C + 1 + D])
    sequence = bits[1 + C + 1 + D + 1]
    result = []

    #print "Combos:", combos
    #print "Destructs:", destructs
    
    for char in sequence:
        result.append(char)
        if len(result) >= 2:
            if combos.has_key((result[-1],result[-2])):
                #print "Combo detected:", result[-1], result[-2]
                product = combos[(result[-1],result[-2])]
                result.pop()
                result.pop()
                result.append(product)
            else:
                #print result
                clear = False
                for el in range(len(result)-1):
                    if destructs.has_key(result[el]) and char in destructs[result[el]]:
                        clear = True
                        break
                if clear:
                    result = []

    answer = "Case #{0}: [".format(t+1)
    for i in range(len(result)):
        if (i > 0):
            answer += ", "
        answer += result[i]
    answer += "]"
    print answer
        
        
    
