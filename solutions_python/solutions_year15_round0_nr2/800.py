import math

f = open('B-small-attempt1.in', 'r')
#f = open('in.txt', 'r')
out = open('out44.txt', 'w')
T = int(f.readline())

def bruteforce(kluce, pocty, cas):
    if (len(kluce) == 0):
        return cas
    else:
        newpocty = {}
        kluce2 = []

        for p in pocty:
            if p > 1:
                newpocty[p - 1] = pocty[p]
                kluce2.append(p - 1)

        min = bruteforce(list(kluce2), dict(newpocty), cas + 1)

        for k in kluce:
            if k > 3:
                a = k // 2
                b = k - a

                pocty2 = dict(pocty)
                kluce2 = list(kluce)
                sec = pocty2[k]
                if a in pocty2:
                    pocty2[a] += pocty2[k]
                else:
                    pocty2[a] = pocty2[k]
                    kluce2.append(a)

                if b in pocty2:
                    pocty2[b] += pocty2[k]
                else:
                    pocty2[b] = pocty2[k]
                    kluce2.append(b)

                kluce2.remove(k)
                del pocty2[k]

                min3 = bruteforce(list(kluce2), dict(pocty2), cas + sec)

                if min3 < min:
                    min = min3

        for k in kluce:
            if k > 3:
                a = k // 3
                b = k - a

                pocty2 = dict(pocty)
                kluce2 = list(kluce)
                sec = pocty2[k]
                if a in pocty2:
                    pocty2[a] += pocty2[k]
                else:
                    pocty2[a] = pocty2[k]
                    kluce2.append(a)

                if b in pocty2:
                    pocty2[b] += pocty2[k]
                else:
                    pocty2[b] = pocty2[k]
                    kluce2.append(b)

                kluce2.remove(k)
                del pocty2[k]

                min3 = bruteforce(list(kluce2), dict(pocty2), cas + sec)

                if min3 < min:
                    min = min3

        return min

for case in range(T):
    line = f.readline()
    D = int(line)
    line = f.readline()
    P = line.strip().split()

    #print(D)
    #print(P)

    pocty = {}
    kluce = []

    for k in P:
        if int(k) in pocty:
            pocty[int(k)] += 1
        else:
            pocty[int(k)] = 1
            kluce.append(int(k))

    kluce.sort(reverse=True)

    min = bruteforce(list(kluce), dict(pocty), 0)

    print(case, min)
    out.write("Case #" + str(case + 1) + ": " + str(min) + "\n")


def nepouzivame():
    sec = 0
    minSec = kluce[0]

    #print(pocty)
    #print(kluce)
    #print(minSec)
    while len(kluce) > 0:
        #print(pocty)
        k = kluce[0]
        if k % 2 == 0:
            sec += pocty[k]

            a = k // 2
            b = k - a

            if a in pocty:
                pocty[a] += pocty[k]
            else:
                pocty[a] = pocty[k]
                kluce.append(a)

            if b in pocty:
                pocty[b] += pocty[k]
            else:
                pocty[b] = pocty[k]
                kluce.append(b)

            kluce.remove(k)
            del pocty[k]

            if len(kluce) > 0:
                kluce.sort(reverse=True)
                if sec + kluce[0] < minSec:
                    minSec = sec + kluce[0]
        else:
            sec += 1
            newpocty = {}
            kluce = []
            for p in pocty:
                if p > 1:
                    newpocty[p - 1] = pocty[p]
                    kluce.append(p - 1)

            pocty = newpocty
            kluce.sort(reverse=True)

            #for i in range(len(kluce) - 2, 0, -1):
            #    tmp = pocty[kluce[i]]
            #    del pocty[kluce[i]]
            #    kluce[i] = kluce[i] - 1
            #    pocty[kluce[i]] = tmp
            #kluce.pop(0)


    print(case, minSec)

    out.write("Case #" + str(case + 1) + ": " + str(minSec) + "\n")


