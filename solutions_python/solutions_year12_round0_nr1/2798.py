mapa = {' ' : ' ', 
        'a' : 'y', 
        'b' : 'h',
        'c' : 'e',
        'd' : 's',
        'e' : 'o',
        'f' : 'c',
        'g' : 'v',
        'h' : 'x',
        'i' : 'd',
        'j' : 'u',
        'k' : 'i',
        'l' : 'g',
        'm' : 'l',
        'n' : 'b',
        'o' : 'k',
        'p' : 'r',
        'q' : 'z',
        'r' : 't',
        's' : 'n',
        't' : 'w',
        'u' : 'j',
        'v' : 'p',
        'w' : 'f',
        'x' : 'm',
        'y' : 'a',
        'z' : 'q'}

t = input()

for i in range(t):
    linha = raw_input()
    nova_linha = ""
    for caractere in linha:
        nova_linha += mapa[caractere]
    print "Case #%d: %s" % (i + 1, nova_linha)


