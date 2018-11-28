#!/usr/bin/python
import sys

def multiply(signA, A, signB, B):
    if A == '1':
        resSign = signB * signA
        res = B
    elif B == '1':
        resSign = signB * signA
        res = A
    elif A == B:
        resSign = -1 * signA * signB
        res = '1'
    elif A == 'i' and B == 'j':
        resSign = signB * signA
        res = 'k'
    elif A == 'i' and B == 'k':
        resSign = -1 * signA * signB
        res = 'j'
    elif A == 'j' and B == 'i':
        resSign = -1 * signA * signB
        res = 'k'
    elif A == 'j' and B == 'k':
        resSign = 1 * signA * signB
        res = 'i'
    elif A == 'k' and B == 'i':
        resSign = 1 * signA * signB
        res = 'j'
    elif A == 'k' and B == 'j':
        resSign = -1 * signA * signB
        res = 'i'
    return  resSign, res


def list_mult(inp):
    if len(inp) == 1:
        return inp[0]
    #if len(inp) == 0:
        #print "Error!"
    A = inp[0]
    inp = inp[1:]
    resSign = 1
    res = A
    for let in inp:
        resSign, res = multiply(resSign, res, 1, let)
    if resSign == -1:
        return 'X'
    else:
        return res

    #print resSign
    #print res


def can_ijk(inp):
    if inp == 'ijk':
        return 'YES'
    elif len(inp) < 3:
        return 'NO'
    else:
        resI = '1'
        resSignI = 1
        resK = '1'
        resSignK = 1
        iPos = list()
        kPos = list()
        for i in range(len(inp)-2):
            resSignI, resI = multiply(resSignI, resI, 1, inp[i])
            if resI == 'i' and resSignI == 1:
                iPos.append(i)
                break
                #if 'jiji' in inp:
                #    print 'I hit:' + ''.join(inp[:i+1])
        if not iPos:
            return 'NO' # Found no i's
        for k in range(len(inp)-1,iPos[0]+1, -1):
            try:
                resSignK, resK = multiply(1, inp[k], resSignK, resK)
            except:
                #print k
                #print len(inp)
                sys.exit(0)
            if resK == 'k' and resSignK == 1:
                #if 'jiji' in inp:
                #    print 'K hit:' + ''.join(inp[k:])
                kPos.append(k)
                break
                #resJ = '1'
                #resSignJ = 1
                ##print 'Yay!' + ''.join(inp[:i+1])
                #for j in range(i+1,len(inp)):
                #    resSignJ, resJ = multiply(resSignJ, resJ, 1, inp[j])
                #    #print "trying"
                #    #print inp[i:j+1]
                #    if resJ  == 'j' and resSignJ == 1 and list_mult(list(inp[j+1:])) == 'k':
                #        #print "YAY!" + ''.join(inp[i+1:j+1])
                #        #print "YAY!" + ''.join(inp[j+1:])
                #        return 'YES'
        if not kPos:
            return 'NO'
        if kPos[0] <= iPos[0] - 1:
            return 'NO'

        if list_mult(inp[iPos[0]+1:kPos[0]]) == 'j':
            return 'YES'
        else:
            return 'NO'
        for jStart in iPos:
            resJ = '1'
            resSignJ = 1
            for j in range(jStart+1,kPos[0]):
                resSignJ, resJ = multiply(1, inp[j], resSignJ, resJ)
                if resSignJ == 1 and resJ == 'j' and j+1 in kPos:
                    return 'YES'
                #if (jEnd - jStart) > 1:
                #    if list_mult(inp[jStart+1:jEnd]) == 'j':
                #        return 'YES'

        return 'NO'


f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
cases = int(lines[0])
lines = lines[1:]
case_num = 1
line_id = 0
mult = 0
for i,line in enumerate(lines):
    if i % 2 == 0:
        mult = int(line.split()[1])
    else:
        if len(line.strip()) == 1:       
            print "Case #{:}: {:}".format(case_num, "NO")
        else:
            print "Case #{:}: {:}".format(case_num, can_ijk(line.strip()*mult))
        sys.stdout.flush()
        case_num += 1

