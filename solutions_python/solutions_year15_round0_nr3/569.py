from sys import argv

def readInput(fl):
    inputs = []
    for ln in open(fl).readlines():
        inputs.append(ln.strip())
    return int(inputs[0]), inputs[1:]

def mul(x, y):
    if x[1] == 1:
        return (x[0] * y[0], y[1])
    elif y[1] == 1:
        return (x[0] * y[0], x[1])
    elif x[1] == y[1]:
        return (-1 * x[0] * y[0], 1)
    elif x[1] == 'i':
        if y[1] == 'j': return (x[0] * y[0], 'k')
        elif y[1] == 'k': return (-1 * x[0] * y[0], 'j')
    elif x[1] == 'j':
        if y[1] == 'i': return (-1 * x[0] * y[0], 'k')
        elif y[1] == 'k': return (x[0] * y[0], 'i') 
    elif x[1] == 'k':
        if y[1] == 'i': return (x[0] * y[0], 'j')
        elif y[1] == 'j': return (-1 * x[0] * y[0], 'i')

def prepareI(chars):
    while len(chars) > 1 and chars[0] != (1, 'i'):
        chars[0] = mul(chars[0], chars[1])
        del chars[1]

def prepareK(chars):
    while len(chars) > 1 and chars[-1] != (1, 'k'):
        chars[-1] = mul(chars[-2], chars[-1])
        del chars[-2]

def getNextIindex(chars, curIndex):
    temp = (1, 'i')
    for idx in range(curIndex + 1, len(chars)):
        temp = mul(temp, chars[idx])
        if temp == (1, 'i'):
            return idx
    return -1

def getNextKindex(chars, curIndex):
    temp = (1, 'k')
    for idx in reversed(range(curIndex)):
        temp = mul(temp, chars[idx])
        if temp == (1, 'k'):
            return idx
    return -1

def aggregate(lst):
    temp = lst[0]
    if len(lst) > 1:
        for i in range(1, len(lst)):
            temp = mul(temp, lst[i])
    return temp

def solve(n_case, n_repeat, string):
    result = 'NO'
    chars = [(1, s) for s in string] * n_repeat
    prepareI(chars)
    prepareK(chars)
    iIndex = 0
    kIndex = len(chars) - 1

    midchar = tuple()
    if len(chars) > 2 and kIndex - iIndex > 1:
        midchar = aggregate(chars[iIndex + 1:kIndex])
        if midchar == (1, 'j'): result = 'YES'
    else:
        midchar_i = midchar
        while kIndex - iIndex > 1 and midchar_i != (1, 'j'):
            temp_kIndex = len(chars) - 1
            midchar_k = midchar_i
            while temp_kIndex - iIndex > 1 and temp_kIndex > -1 and midchar_k != (1, 'j'):
                temp_k = getNextKindex(chars, temp_kIndex)
                if temp_k < 0: break
                #update midchark
                residue = aggregate(chars[temp_k:temp_kIndex])
                midchar_k = mul(midchar_k, (residue[0] * -1, residue[1]))
                temp_kIndex = temp_k
            if midchar_k == (1, 'j'): 
                kIndex = temp_kIndex
                result = 'YES'
                break
            temp_i = getNextIindex(chars, iIndex)
            if temp_i < iIndex: break
            #update midcahari
            residue = aggregate(chars[iIndex+1:temp_i+1])
            midchar_i = mul(midchar_i, (residue[0] * -1, residue[1]))
            iIndex = temp_i
    print 'Case #%d: %s' % (n_case + 1, result)

if __name__ == '__main__':
    n_cases, inputs = readInput(argv[1])
    for n_case in range(n_cases):
        solve(n_case, int(inputs[n_case * 2].split()[1]), inputs[n_case * 2 + 1])
