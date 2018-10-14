
def can_be(score, max_value):
    return (max_value - 1) * 2 + max_value <= score

def can_be_sup(score, max_value):
    if max_value == 1: return score >= 1
    return (max_value - 2) * 2 + max_value <= score

f = open('test')
cases = int(f.readline())

for cas in range(cases):
    lista = f.readline().split()
    lista = [int(x) for x in lista]
    N = lista[0]
    S = lista[1]
    p = lista[2]
    counter = 0
    S_used = 0

    for x in range(3, len(lista)):
        if can_be(lista[x], p):
            counter += 1
        else:
            if can_be_sup(lista[x], p) and S_used < S:
                S_used += 1
                counter += 1
    print "Case #%s: %s" % (cas + 1, counter)


