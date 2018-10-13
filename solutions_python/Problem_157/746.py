multiplicationDict = {'ii':(-1,''),'jj':(-1,''), 'kk':(-1,''),'ij':(1,'k'), 'ik':(-1,'j'), 'jk':(1,'i'),
        'ji':(-1,'k'), 'ki':(1, 'j'), 'kj':(-1,'i')}

def findFirst(string, letter, sign = 1, pos = 0):
    while len(string) > 0:
        if string[0] == letter:
            return sign, pos
        if len(string) == 1:
            return sign, None
        res = multiplicationDict[string[:2]]
        pos += 2 - len(res[1])
        sign *= res[0]
        string = res[1] + string[2:]
    return sign, None

def productOfString(string, sign = 1):
    if len(string) <= 1:
        return string, sign

    if len(string) == 2:
        res = multiplicationDict[string]
        sgn, strRes = res[0], res[1]
        sign *= sgn
        return strRes, sign
    else:
        subString1, sign1 = productOfString(string[:len(string)/2], sign)
        subString2, sign2 = productOfString(string[len(string)/2:], sign)
        sign = sign*sign1*sign2
        return productOfString(subString1 + subString2, sign)

for case in range(int(raw_input())):
    output = "Case #%d: " % (case + 1)
    line = raw_input().split(' ')
    l, x = int(line[0]), int(line[1])
    string = raw_input()
    assert(len(string)==l)
    totalString = string*x
    assert(len(totalString) == l*x)

    sign1, pos = findFirst(totalString[:min(2,x)*l], 'i')
    if pos is None:
        output += 'NO'
        print output
        continue
    totalString = totalString[pos+1:]

    sign2, pos = findFirst(totalString[:min(2,x)*l], 'j')
    if pos is None:
        output += 'NO'
        print output
        continue
    totalString = totalString[pos+1:]

    resString, sign3 = productOfString(totalString)
    if sign1*sign2*sign3 == 1 and resString == 'k':
        output += 'YES'
    else:
        output += 'NO'
    print output
