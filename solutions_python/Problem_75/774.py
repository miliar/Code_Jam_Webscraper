def Simplify(elements, combine, opposed):
    repeat = True
    while repeat:
        repeat = False
        # Check combinations
        for combination in combine:
            try:
                if combination[0] == elements[-1] and combination[1] == elements[-2] or combination[1] == elements[-1] and combination[0] == elements[-2]:
                    elements = elements[:-2] + combination[2]
                    repeat = True
            except:
                pass
        if repeat:
            continue
        # Check opposition
        for opposition in opposed:
            a = False
            b = False
            for i in elements:
                if i == opposition[0]:
                    a = True
                if i == opposition[1]:
                    b = True
            if a and b:
                elements = ""
                repeat = True
    return elements

def Invoke(elements, combine, opposed):
    result = ""
    for i in elements:
        result += i
        result = Simplify(result, combine, opposed)
    return result

fin = file("magicka.in")
line = fin.readlines()
for i in range(1, int(line[0]) + 1):
    case = line[i].strip().split(" ")
    j = 0
    comb = []
    for k in range(int(case[j])):
        j += 1
        comb += [case[j]]
    j += 1
    oppo = []
    for k in range(int(case[j])):
        j += 1
        oppo += [case[j]]
    print "Case #" + str(i) + ": " + str([l for l in Invoke(case[-1], comb, oppo)]).replace("'", "")
