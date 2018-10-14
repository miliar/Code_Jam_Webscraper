
def permuta( nn, a, b, ok ):

    s = str(nn)
    sn = nn

    news = s
    testme = []

    count = 0
    for i in range(1,len(s)):
        news = news[1:] + news[0]
        if ok[news[0]]: # fc >= first_a and fc <= first_b:
           newn = int(news)
           if newn > sn and newn <= b and newn not in testme:
              testme.append(newn)
              count += 1

    return count

n = int(input())
# print n
prev_cases = {}
for i in range(n):
    values = raw_input().split()
    a_str = values[0]
    b_str = values[1]
    key = a_str + ":" + b_str
    if key in prev_cases:
       print "Case #"+str(i+1) + ":", prev_cases[key]
#       print "Used cache"
       continue

    a = int(a_str)
    b = int(b_str)
    l = len(a_str)
    # print a, b, l
    # print "Numero inicial: ", numbers, " ---------"

    # Para descartar algunos casos mas rapidamente
    # se compara el primer caracter del numero que se revisa
    # Si el primer caracter no esta entre los limites, el nro
    # se puede descartar inmediatamente
    # (Los numeros a revisar son aquellos que se generan cuando
    #  se shiftea el numero actual, que se guarda en nn)
    first_a = int(a_str[0])
    first_b = int(b_str[0])
    ok = {} # [ False for x in range(10) ]
    for j in range(10):
        ok[str(j)] = ((j>=first_a) and (j<=first_b))

    contar = 0
    nn = a 
    while nn <= b: 
        # revisar el numero actual a ver si las transformaciones se pueden contar
        contar += permuta( nn, a, b, ok )
        nn += 1
    print "Case #"+str(i+1) + ":", contar
    prev_cases[key] = contar

