def mult(a,b):
    res = ''
    if a.strip('-') == '1':
        res = b.strip('-')
    elif b.strip('-') == '1':
        res = a.strip('-')
    else:
        reala = a.strip('-')
        realb = b.strip('-')
        if reala == realb:
            res = '-1'
        else:
            if reala == 'i':
                if realb == 'j':
                    res = 'k'
                elif realb == 'k':
                    res = '-j'
            elif reala == 'j':
                if realb == 'i':
                    res = '-k'
                elif realb == 'k':
                    res = 'i'
            elif reala == 'k':
                if realb == 'i':
                    res = 'j'
                elif realb == 'j':
                    res = '-i'
    if (('-' in a) and ('-' not in b)) or (('-' in a) and ('-' not in b)):
        if res[0] == '-':
            res = res[1]
        else:
            res = '-' + res
    return res
    
cases = int(input())

for casoactual in range(cases):
    L,X = [int(i) for i in input().split()]
    palabra = input() * X
    if L == 1:
        print('Case #' + str(casoactual + 1) + ': NO')
    else:
        currentres = '1'
        rango = ['i','j','k']
        proceso = 0
        end = False
        for letter in range(len(palabra)):
            currentres = mult(currentres,palabra[letter])
            if (end == False) and currentres == rango[proceso]:
                proceso = proceso + 1
                currentres = '1'
                if proceso >= 3:
                    end = True
        if end and currentres == '1':
            print('Case #' + str(casoactual + 1) + ': YES')
        else:
            print('Case #' + str(casoactual + 1) + ': NO')
