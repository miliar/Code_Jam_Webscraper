def filter(palavras, letras, pos):
    result = []
    for p in palavras:
        if p[pos] in letras:
            result.append(p)
    return result

fp = open('first.in', 'r')
parms = [int(x) for x in fp.readline().split()]

palavras = []
for x in range(parms[1]):
    palavras.append(fp.readline().strip())

#palavras.sort()

case = 1
for x in range(parms[2]):
    pattern = fp.readline().strip()
    
    i = 0
    pos = 0
    result = palavras
    while i < len(pattern):
        letras = []
        if pattern[i] == '(':
            i += 1
            while pattern[i] != ')':
                letras.append(pattern[i])
                i += 1
        else:
            letras.append(pattern[i])
        
        result = filter(result, letras, pos)
        
        i += 1
        pos += 1
    
    print 'Case #' + str(case) + ': ' + str(len(result))
    case += 1
