#!/usr/bin/python

def baseNto10(num, base):
    exponente = len(num) - 1
    result = 0
    for i in num:
        result += (base**exponente)*i
        exponente -= 1
    return result

for case in range(input()):
    num = raw_input()
    num_l = list(num)
    num_s = list(set(num_l))
    base = len(num_s)
    if (base < 2):
        base = 2
    tradc = {}
    tradc[num_l[0]] = 1
    sol = [1]
    i = 1
    while (i< len(num_l)) and (num_l[0] == num_l[i]):
        sol.append(1)
        i += 1
    if (i < len(num_l)):
        tradc[num_l[i]] = 0
        sol.append(0)
        base_i = 2
        for c in range(len(sol), len(num_l)):
            if (num_l[c] in tradc):
                sol.append(tradc[num_l[c]])
            else:
                tradc[num_l[c]] = base_i
                sol.append(base_i)
                base_i += 1
        if (base_i != base):
            print 'Error al asignar digitos, hemos asignado de mas o de menos'

    print 'Case #%s: %s' % (case + 1, baseNto10(sol, base))


